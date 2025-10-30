import os
from pathlib import Path
from dotenv import load_dotenv
from alpaca_trade_api.rest import REST

# Manually load the .env file from your current project folder
dotenv_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path)

# Get credentials
API_KEY = os.getenv("APCA_API_KEY_ID")
SECRET_KEY = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = os.getenv("APCA_API_BASE_URL")

# Print check (just for debugging)
print("API_KEY:", API_KEY)
print("SECRET_KEY:", SECRET_KEY)
print("BASE_URL:", BASE_URL)

# Initialize API (only if keys exist)
if not API_KEY or not SECRET_KEY:
    raise ValueError("API keys not found. Check your .env file and its path.")

api = REST(API_KEY, SECRET_KEY, base_url=BASE_URL)

# Test connection by getting account info
account = api.get_account()
print(f"✅ Connected to Alpaca! Account status: {account.status}")
