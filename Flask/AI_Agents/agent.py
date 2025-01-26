# from agent import fiance_agent
# from phi.agent import Agent
# from phi.model.groq import Groq
import re
from joblib import load
import asyncio
import yfinance as yf
from stock_updater import fetch_stock_details
# from phi.tools.yfinance import YFinanceTools  # Replace with actual library import

# finance_agent = Agent(
#     name="Finance Agent",
#     model=Groq(id="llama-3.3-70b-versatile"),
#     tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
#     instructions=["display only recommendation in json format"],
#     show_tool_calls=True,
#     markdown=True
# )

async def recommend(symbol: str):
    try:
        # data = []
        data = await fetch_stock_details(symbol)
        return  data

    except Exception as e:
        print(f"Err: {e}")
