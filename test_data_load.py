from finrl.config_tickers import DOW_30_TICKER

from config.config import DOW_30, TRAIN_START_DATE, TRADE_END_DATE
from preprocessing.data_loader import load_or_fetch_data

if __name__ == "__main__":
    df = load_or_fetch_data(DOW_30, TRAIN_START_DATE, TRADE_END_DATE)
    print(df.head())
    print(f"Loaded {len(df)} rows.")

    print("Unique tickers per date in the data.csv:")
    print(df.groupby('date')['tic'].nunique().value_counts().sort_index())

    print(sorted(DOW_30_TICKER))
    print("Total number of tickers in DJIA30:", len(DOW_30_TICKER))

    # Find missing tickers
    expected = set(DOW_30_TICKER)
    actual = set(df['tic'].unique())
    missing = expected - actual
    print("Missing ticker(s):", missing)






