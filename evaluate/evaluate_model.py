from finrl.plot import get_baseline, backtest_stats
import pandas as pd
import matplotlib.pyplot as plt

def evaluate_and_plot(model, env, baseline_ticker, start, end, output_dir, mode="test"):
    account_value, actions, states = model.DRL_prediction(model=model, environment=env)
    actions.to_csv(f"{output_dir}/{mode}_actions.csv")
    states.to_csv(f"{output_dir}/{mode}_state.csv")

    perf = pd.DataFrame(backtest_stats(account_value=account_value))
    perf.columns = ['Value']
    perf.to_csv(f"{output_dir}/perf_stats_{mode}.csv")

    # Compare with DJIA
    dji_df = get_baseline(ticker=baseline_ticker, start=start, end=end)
    fst_day = dji_df["close"].iloc[0]
    dji = dji_df["close"] / fst_day * 1000000

    result = pd.DataFrame({
        "a2c": account_value.set_index(account_value.columns[0])["account_value"],
        "dji": dji.values
    })

    result.to_csv(f"{output_dir}/{mode}_result.csv")
    result.plot(figsize=(15, 10), title=f"{mode.upper()} Performance")
    plt.legend(loc='upper right')
    plt.savefig(f"{output_dir}/profit_{mode}.png")
    plt.clf()
