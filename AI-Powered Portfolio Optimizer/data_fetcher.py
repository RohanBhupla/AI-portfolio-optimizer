# data_fetcher.py
# 🧠 Purpose: Fetch and save stock data from the Alpaca Markets API
# Author: Rohan Bhupla

import os
import pandas as pd
from dotenv import load_dotenv
from alpaca_trade_api import REST, TimeFrame

# 1️⃣ Load environment variables
load_dotenv()

API_KEY = os.getenv("APCA_API_KEY_ID")
SECRET_KEY = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = os.getenv("APCA_API_BASE_URL")

# 2️⃣ Initialize API connection
api = REST(API_KEY, SECRET_KEY, base_url=BASE_URL)

# 3️⃣ Fetch stock data for a single symbol
def get_stock_data(symbol: str, days: int = 5):
    print(f"Fetching data for {symbol} over the last {days} days...")
    bars = api.get_bars(symbol, TimeFrame.Day, limit=days).df
    bars = bars[["open", "high", "low", "close", "volume"]]
    print(f"Retrieved {len(bars)} data points for {symbol}.")
    return bars

# 4️⃣ Fetch multiple tickers and save them to CSV
def fetch_and_save(symbols, days=5):
    os.makedirs("data", exist_ok=True)  # create data folder if not exists
    for symbol in symbols:
        df = get_stock_data(symbol, days)
        file_path = f"data/{symbol}.csv"
        df.to_csv(file_path)
        print(f"✅ Saved {symbol} data to {file_path}\n")

# 5️⃣ Run test
if __name__ == "__main__":
    symbols_to_fetch = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]
    fetch_and_save(symbols_to_fetch, days=5)
