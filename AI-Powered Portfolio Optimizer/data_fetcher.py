# data_fetcher.py
# 🧠 Purpose: Fetch stock data from the Alpaca Markets API
# Author: Rohan Bhupla

import os
from dotenv import load_dotenv
from alpaca_trade_api import REST, TimeFrame

# 1️⃣ Load environment variables
load_dotenv()

API_KEY = os.getenv("APCA_API_KEY_ID")
SECRET_KEY = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = os.getenv("APCA_API_BASE_URL")

# 2️⃣ Initialize API connection
api = REST(API_KEY, SECRET_KEY, base_url=BASE_URL)

# 3️⃣ Function to fetch recent stock data
def get_stock_data(symbol: str, days: int = 5):
    """
    Fetch historical stock data for a given symbol.
    
    :param symbol: Stock symbol (e.g., "AAPL", "TSLA")
    :param days: Number of days of data to fetch
    :return: Pandas DataFrame with price history
    """
    print(f"Fetching data for {symbol} over the last {days} days...")
    
    bars = api.get_bars(
        symbol,
        TimeFrame.Day,
        limit=days
    ).df  # Convert to pandas DataFrame automatically
    
    # Optional: Only return relevant columns
    bars = bars[["open", "high", "low", "close", "volume"]]
    
    print(f"Retrieved {len(bars)} data points for {symbol}.")
    return bars

# 4️⃣ Test run (only runs when you execute this file directly)
if __name__ == "__main__":
    df = get_stock_data("AAPL", 5)
    print(df)
