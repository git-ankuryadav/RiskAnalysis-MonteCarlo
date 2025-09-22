import numpy as np
import pandas as pd

import numpy as np

def estimate_jump_params(log_returns, threshold_std=3, trading_days=252):
    # Compute volatility excluding jumps
    vol = np.std(log_returns)
    
    # Identify jumps as returns where abs > threshold * vol
    jumps_idx = np.where(np.abs(log_returns) > threshold_std * vol)[0]
    jump_returns = log_returns[jumps_idx]
    
    # Estimate lambda: jumps per year
    total_days = len(log_returns)
    years = total_days / trading_days
    lamb = len(jump_returns) / years
    
    # Estimate jump size mean and std (using jump returns directly)
    mu_j = np.mean(jump_returns)
    sigma_j = np.std(jump_returns)
    
    return lamb, mu_j, sigma_j


# lamb, mu_j, sigma_j = estimate_jump_params(log_returns)


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
