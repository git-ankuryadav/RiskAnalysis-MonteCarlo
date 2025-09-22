import numpy as np
import pandas as pd

import numpy as np

def jump_diffusion_simulation(S0, mu, sigma, T, steps, paths, 
                              lamb, mu_j, sigma_j):
    """
    Simulate price paths with Jump Diffusion model.

    Parameters:
    - S0: initial price
    - mu: drift
    - sigma: volatility
    - T: time horizon (years)
    - steps: number of steps
    - paths: number of simulated paths
    - lamb: jump intensity (expected jumps per year)
    - mu_j: mean of jump size in log-space
    - sigma_j: volatility of jump size in log-space

    Returns:
    - numpy array of shape (steps+1, paths) with simulated prices
    """
    dt = T / steps
    drift = (mu - lamb * (np.exp(mu_j + 0.5 * sigma_j**2) - 1)) * dt
    diffusion = sigma * np.sqrt(dt)

    price_paths = np.zeros((steps + 1, paths))
    price_paths[0] = S0

    for t in range(1, steps + 1):
        Z = np.random.standard_normal(paths)
        # Number of jumps in dt ~ Poisson
        N = np.random.poisson(lamb * dt, paths)
        # Jump sizes (log-normal)
        Y = np.exp(np.random.normal(mu_j, sigma_j, paths))  # if jump occurs
        
        jump_component = np.where(N > 0, Y**N, 1.0)  # if no jump, multiplier=1

        price_paths[t] = price_paths[t-1] * np.exp(drift + diffusion * Z) * jump_component

    return price_paths


def monte_carlo_simulation(S0, mu, sigma, T, steps, paths):
    """
    Simulate future stock price paths using Geometric Brownian Motion.

    Parameters:
    - S0: Initial stock price
    - mu: Annualized drift
    - sigma: Annualized volatility
    - T: Total time horizon in years (e.g., 1/12 for 1 month)
    - steps: Number of time steps (e.g., trading days)
    - paths: Number of simulated paths

    Returns:
    - A (steps+1) x paths numpy array of simulated price paths
    """
    dt = T / steps
    mu_daily = mu / 252
    sigma_daily = sigma / np.sqrt(252)

    # Pre-allocate price paths array
    price_paths = np.zeros((steps + 1, paths))
    price_paths[0] = S0

    # Simulation of paths
    for t in range(1, steps + 1):
        Z = np.random.standard_normal(paths)
        price_paths[t] = price_paths[t-1] * np.exp(
            (mu_daily - 0.5 * sigma_daily**2) * dt + sigma_daily * np.sqrt(dt) * Z
        )

    return price_paths

if __name__ == "__main__":
    from parameter_estimation import estimate_params
    

    df = pd.read_csv("../data/historicalData.csv")
    mu, sigma = estimate_params(df)

    # Set simulation parameters
    S0 = df['Closing_Price'].iloc[-1]  # last closing price
    T = 1/12  # 1 month in years
    steps = 21  # roughly 21 trading days in a month
    paths = 1000  # number of simulated paths

    simulated_paths = monte_carlo_simulation(S0, mu, sigma, T, steps, paths)

    # Convert to DataFrame for convenience (optional)
    sim_df = pd.DataFrame(simulated_paths.T)
    print(sim_df.head())