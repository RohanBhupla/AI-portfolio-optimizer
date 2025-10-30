import os
from pathlib import Path
from dotenv import load_dotenv
import pandas as pd
from alpaca_trade_api.rest import REST, TimeFrame

# Load .env
dotenv_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path)

# Get credentials
API_KEY = os.getenv("APCA_API_KEY_ID")
SECRET_KEY = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = os.getenv("APCA_API_BASE_URL")

# Initialize API
api = REST(API_KEY, SECRET_KEY, base_url=BASE_URL)

# Define stock symbols and timeframe
symbols = ["AAPL", "MSFT", "TSLA"]
timeframe = TimeFrame.Day  # daily bars

# Fetch historical data
for symbol in symbols:
    print(f"Fetching data for {symbol}...")
    bars = api.get_bars(symbol, timeframe, limit=100).df  # last 100 days
    bars.to_csv(f"{symbol}_data.csv")
    print(f"{symbol} data saved to {symbol}_data.csv")
