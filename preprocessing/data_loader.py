import os
import pandas as pd
import numpy as np
from finrl.meta.preprocessor.yahoodownloader import YahooDownloader
from finrl.meta.preprocessor.preprocessors import FeatureEngineer
from finrl.config import INDICATORS

def load_or_fetch_data(ticker_list, start_date, end_date, filename='./data/data.csv'):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    if os.path.exists(filename):
        print(f"Loading cached data from {filename}")
        return pd.read_csv(filename, index_col=0)

    print(f"Downloading new data from Yahoo Finance...")
    df = YahooDownloader(
        start_date=start_date,
        end_date=end_date,
        ticker_list=ticker_list
    ).fetch_data()

    fe = FeatureEngineer(
        use_technical_indicator=True,
        tech_indicator_list=INDICATORS,
        use_vix=True,
        use_turbulence=True,
        user_defined_feature=False
    )

    processed = fe.preprocess_data(df)
    processed = processed.fillna(0).replace([np.inf, -np.inf], 0)
    processed.to_csv(filename)
    print(f"Saved processed data to {filename}")
    return processed
