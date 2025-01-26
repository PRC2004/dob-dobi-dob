# Imports
from flask import Flask, request, jsonify, render_template, redirect
from dotenv import load_dotenv
# from AI_Agents.agent import finance_agent, recommend
import stock_updater
import re
import threading
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
        score = recommend(stock_name)
        if type(score) == str:
            return "Error"
        else :
            return jsonify({"Stock": stock_name, "Score": score})
        # response = finance_agent.run(f"Analyst recommendation on {stock_name}", stream=False)
        # print(response.content)
        # cleaned_String = re.findall(r"\*\s+(.*?):\s(\d+)", response.content)
        # if cleaned_String:
        #     recommendation_dict = {label: int(value) for label, value in cleaned_String}
        #     # print(recommendation_dict)
        #     return jsonify({"stock": stock_name, 'Stock_Score': recommendation_dict}), 200
        # else:
        #     return jsonify({"message": "Error Getting data"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    updater_thread = threading.Thread(target=stock_updater.start_background_updater, daemon=True)
    updater_thread.start()
    app.run(debug=True)
