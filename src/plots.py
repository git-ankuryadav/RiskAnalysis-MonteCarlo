import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot_simulated_prices(simulated_prices, num_paths=50):
    """
    Plot simulated stock price paths.
    Shows a subset of paths to avoid clutter.
    """
    plt.figure(figsize=(12,6))
    for i in range(min(num_paths, simulated_prices.shape[1])):
        plt.plot(simulated_prices[:, i], lw=0.7, alpha=0.7)
    plt.title("Simulated Stock Price Paths")
    plt.xlabel("Time Steps (Days)")
    plt.ylabel("Price")
    plt.grid(True)
    plt.show()


def plot_returns_histogram(simulated_prices, initial_price, confidence_levels=[0.95, 0.99]):
    """
    Plot histogram of simulated returns with VaR and Expected Shortfall marked.
    """
    final_prices = np.array(simulated_prices[-1, :], dtype=np.float64)
    initial_price = float(initial_price)
    returns = (final_prices - initial_price) / initial_price

    plt.figure(figsize=(12,6))
    plt.hist(returns, bins=50, alpha=0.7, color='skyblue')
    plt.title("Histogram of Simulated Returns at Horizon")
    plt.xlabel("Return")
    plt.ylabel("Frequency")

    for cl in confidence_levels:
        var = np.percentile(returns, (1 - cl) * 100)
        es = returns[returns <= var].mean()
        plt.axvline(var, color='r', linestyle='--', label=f'{int(cl*100)}% VaR: {var:.4f}')
        plt.axvline(es, color='m', linestyle='--', label=f'{int(cl*100)}% ES: {es:.4f}')

    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Assuming you have `simulated_paths` and `S0` from previous steps
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

    # Example calls:
    # plot_simulated_prices(simulated_paths, num_paths=1000)
    plot_returns_histogram(simulated_paths, S0, confidence_levels=[0.95, 0.99])
