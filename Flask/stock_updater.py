import yfinance as yf
import asyncio
import aiohttp
import re
from datetime import datetime
import pandas as pd
from constants import stock_symbols

global stock_data
stock_data = []

async def fetch_stock_details(symbol: str):
    try:
        ticker = yf.Ticker(symbol)
        price = ticker.history(period="1d")['Close'][-1]
        description = ticker.info.get("longBusinessSummary", "Description not available")
        # score = recommend(symbol)
        return {
            "symbol": symbol,
            "price": price,
            "description": description,
            # "Score": score,
            "timestamp": datetime.now()
        }
        # print(f"{symbol} == {score}")
        # if type(score) != str:
        #     return {
        #         "symbol": symbol,
        #         "price": price,
        #         "description": description,
        #         "Score": score,
        #         "timestamp": datetime.now()
        #     }
        # else :
        #     return {
        #         "symbol": symbol,
        #         "price": price,
        #         "description": description,
        #         "Score": "Failed",
        #         # "news": news,
        #         "timestamp": datetime.now(),
        #     }
    except Exception as e:
        print(f"Failed to fetch data for {symbol}: {e}")
        # return {
        #     "symbol": symbol,
        #     "price": None,
        #     "description": None,
        #     # "news": None,
        #     "timestamp": datetime.now(),
        # }

async def fetch_all_stock_details():
    """Fetch stock details for all symbols asynchronously."""
    tasks = [fetch_stock_details(symbol) for symbol in stock_symbols]
    results = await asyncio.gather(*tasks)
    stock_data.extend(results)
    # print(results)
    #
        # print(
        #     f"\nSymbol: {item['symbol']}\nPrice: {item['price']}\nDescription: {item['description']}"
        # # News: {item['news']}\n
        # )


async def schedule_updates(interval: int):
    while True:
        print(f"fetching Data at {datetime.now()}...")
        await fetch_all_stock_details()
        await asyncio.sleep(interval)

def start_background_updater():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(schedule_updates(interval=120))

# if __name__ == "__main__":
#     interval_seconds = 60
#     print("Starting...")
#     asyncio.run(schedule_updates(interval_seconds))




# async def fetch_Stock_price():
#     global price_data
#     print(f"Time : {datetime.now()}")

#     for symbol in stock_symbols:
#         try:
#             stock = yf.Ticker(symbol)
#             price = stock.history(period="1d")['Close'][-1]
#             price_data.append({"symbol": symbol, "price": price, "timestamp": datetime.now()})

#         except Exception as e:
#             print(f"Failed to Fetch for {symbol}: {e}")

#     pd.DataFrame(price_data).to_csv("stock_prices.csv", index=False)

# schedule.every(5).minutes.do(fetch_Stock_price)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
