import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# List of symbols
symbols = ["AAPL", "MSFT", "TSLA"]

for symbol in symbols:
    print(f"\nProcessing {symbol}...")
    
    # Load the historical data
    df = pd.read_csv(f"{symbol}_data.csv", index_col=0, parse_dates=True)
    
    # Calculate next-day return
    df['next_return'] = df['close'].shift(-1) - df['close']
    df['target'] = (df['next_return'] > 0).astype(int)  # 1 if price goes up, 0 if down
    
    # Features: use today's open, high, low, close, volume
    features = ['open', 'high', 'low', 'close', 'volume']
    X = df[features].iloc[:-1]  # drop last row (no next day)
    y = df['target'].iloc[:-1]
    
    # Split into train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    
    # Train a simple model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    
    # Predict and evaluate
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy for {symbol}: {acc:.2f}")
