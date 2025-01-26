# Imports
from flask import Flask, request, jsonify, render_template, redirect
from dotenv import load_dotenv
from stock_updater import fetch_stock_details
import stock_updater
import re
import threading
import yfinance as yf
import datetime
# from flask import Flask, request, jsonify
# # from agent import fiance_agent
# from phi.agent import Agent
# from phi.model.groq import Groq
# from phi.tools.yfinance import YFinanceTools  # Replace with actual library import

# Initialize the Flask app
app = Flask(__name__, template_folder="template", static_folder='static')
load_dotenv() # Load Environment variables

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/learn")
def learn():
    return render_template("learn.html")

@app.route("/login")
def login():
    return render_template("login.html")




# Initialize the Finance Agent
# finance_agent = Agent(
#     name="Finance Agent",
#     model=Groq(id="llama-3.3-70b-versatile"),
#     tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
#     instructions=["display only recommendation in json format"],
#     show_tool_calls=True,
#     markdown=True
# )


#   AI Agent Calling for fetching data regarding a particular Stock
@app.route('/recommendation', methods=['GET'])
def get_recommendation():
    stock_name = request.args.get('stock')
    if not stock_name:
        return jsonify({"error": "Missing 'stock' parameter"}), 400

    try:
        ticker = yf.Ticker(stock_name)
        price = ticker.history(period="1d")['Close'][-1]
        description = ticker.info.get("longBusinessSummary", "Description not available")
        return {
            "symbol": stock_name,
            "price": price,
            "description": description,
            # "Score": score,
        }

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    updater_thread = threading.Thread(target=stock_updater.start_background_updater, daemon=True)
    updater_thread.start()
    app.run(debug=True)
