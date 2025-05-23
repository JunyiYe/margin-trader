# import argparse
# from config.config import *
# from preprocessing.data_loader import load_or_fetch_data
# from finrl.meta.preprocessor.preprocessors import data_split
# from train.train_a2c import train_a2c
# from evaluate.evaluate_model import evaluate_and_plot
# from env.margin_trading_env import MarginTradingEnv

# def main(args):
#     set_random_seed(SEED)

#     data = load_or_fetch_data(DOW_30_TICKER, TRAIN_START_DATE, TRADE_END_DATE)
#     train = data_split(data, TRAIN_START_DATE, TRAIN_END_DATE)
#     test = data_split(data, TEST_START_DATE, TEST_END_DATE)
#     trade = data_split(data, TRADE_START_DATE, TRADE_END_DATE)

#     stock_dim = len(train.tic.unique())
#     state_space = 2*3 + 2*stock_dim + len(INDICATOR_LIST)*stock_dim
#     env_kwargs = {
#         "hmax": 100,
#         "initial_amount": 1000000,
#         "num_stock_shares": [0] * stock_dim,
#         "buy_cost_pct": [0.001] * stock_dim,
#         "sell_cost_pct": [0.001] * stock_dim,
#         "state_space": state_space,
#         "stock_dim": stock_dim,
#         "tech_indicator_list": INDICATOR_LIST,
#         "action_space": 2*stock_dim,
#         "reward_scaling": 1e-4,
#         'penalty_sharpe': args.penalty
#     }

#     env_train = MarginTradingEnv(df=train, **env_kwargs).get_sb_env()[0]
#     trained_model = train_a2c(env_train, {
#         'n_steps': args.n_steps,
#         'ent_coef': args.ent_coef,
#         'learning_rate': args.lr,
#         'gamma': args.gamma
#     }, SEED, args.results_dir, args.model_dir)

#     # Evaluate on test and trade sets
#     evaluate_and_plot(trained_model, MarginTradingEnv(df=test, turbulence_threshold=70, risk_indicator_col='vix', **env_kwargs), "^DJI", TEST_START_DATE, TEST_END_DATE, args.results_dir, "test")
#     evaluate_and_plot(trained_model, MarginTradingEnv(df=trade, turbulence_threshold=70, risk_indicator_col='vix', **env_kwargs), "^DJI", TRADE_START_DATE, TRADE_END_DATE, args.results_dir, "trade")

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--n_steps', type=int, default=5)
#     parser.add_argument('--gamma', type=float, default=0.99)
#     parser.add_argument('--lr', type=float, default=0.005)
#     parser.add_argument('--ent_coef', type=float, default=0.005)
#     parser.add_argument('--penalty', type=float, default=0.05)
#     parser.add_argument('--results_dir', type=str, default="results")
#     parser.add_argument('--model_dir', type=str, default="models")
#     args = parser.parse_args()
#     main(args)


# main.py
from config.config import (
    DOW_30, INDICATOR_LIST,
    TRAIN_START_DATE, TRAIN_END_DATE,
    TEST_START_DATE, TEST_END_DATE,
    TRADE_START_DATE, TRADE_END_DATE
)
from preprocessing.data_loader import load_or_fetch_data
from preprocessing.split_data import split_data_by_date

if __name__ == "__main__":
    print("📦 Loading and preprocessing data...")
    data = load_or_fetch_data(DOW_30, TRAIN_START_DATE, TRADE_END_DATE)

    print("🧪 Splitting data into train/test/trade...")
    train, test, trade = split_data_by_date(
        data,
        train_range=(TRAIN_START_DATE, TRAIN_END_DATE),
        test_range=(TEST_START_DATE, TEST_END_DATE),
        trade_range=(TRADE_START_DATE, TRADE_END_DATE)
    )

    print(f"Train set: {train.shape}, Test set: {test.shape}, Trade set: {trade.shape}")
