import numpy as np
import pandas as pd

def calculate_var_es(simulated_prices, initial_price, confidence_levels=[0.95, 0.99]):
    """
    Calculate Value at Risk (VaR) and Expected Shortfall (ES) at specified confidence levels
    from simulated price paths.

    Parameters:
    - simulated_prices: numpy array, shape (steps+1, paths), simulated price paths
    - initial_price: float, the starting price S0
    - confidence_levels: list of floats, confidence levels for VaR/ES calculation

    Returns:
    - dict: keys are confidence levels, values are dicts with 'VaR' and 'ES'
    """
    # Calculate returns at horizon: (final price - initial_price) / initial_price
    final_prices = np.array(simulated_prices[-1, :], dtype=np.float64)
    initial_price = float(initial_price)
    returns = (final_prices - initial_price) / initial_price
    results = {}

    for cl in confidence_levels:
        var = np.percentile(returns, (1 - cl) * 100)
        # Expected Shortfall is the mean of returns worse than VaR
        es = returns[returns <= var].mean()
        results[cl] = {'VaR': var, 'ES': es}
    return results


if __name__ == "__main__":

    from parameter_estimation import estimate_params
    from monte_carlo import monte_carlo_simulation
    

    df = pd.read_csv("../data/historicalData.csv")
    mu, sigma = estimate_params(df)

    # Set simulation parameters
    S0 = df['Closing_Price'].iloc[-1]  # last closing price
    T = 1/12  # 1 month in years
    steps = 21  # roughly 21 trading days in a month
    paths = 1000  # number of simulated paths

    simulated_paths = monte_carlo_simulation(S0, mu, sigma, T, steps, paths)
    sim_df = pd.DataFrame(simulated_paths.T)


    risk_metrics = calculate_var_es(simulated_paths, S0)
    for cl, metrics in risk_metrics.items():
        print(f"Confidence Level: {int(cl*100)}%")
        print(f"  VaR: {metrics['VaR']:.4f}")
        print(f"  Expected Shortfall (ES): {metrics['ES']:.4f}")
