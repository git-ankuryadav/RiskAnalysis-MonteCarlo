import numpy as np
import pandas as pd

def estimate_params(df, return_col='Log_Return', trading_days=252):
 
    mean_return = df[return_col].mean()
    std_return = df[return_col].std()

    mu = mean_return * trading_days
    sigma = std_return * np.sqrt(trading_days)

    return mu, sigma


if __name__ == "__main__":
    

    df = pd.read_csv("../data/historicalData.csv")

    mu, sigma = estimate_params(df)
    print(f"Drift (mu): {mu:.6f}, Volatility (sigma): {sigma:.6f}")
