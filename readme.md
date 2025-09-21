# Monte Carlo Simulation for Risk Analysis on Indian Stocks

This project performs quantitative risk analysis on Indian stock prices using Monte Carlo simulations based on Geometric Brownian Motion (GBM). It estimates potential future price scenarios and downside risk metrics like Value at Risk (VaR) and Expected Shortfall (ES) over a specified time horizon.

---

## Project Overview

The goal is to model possible future price movements of an Indian stock (e.g., Reliance Industries) using historical price data, simulate many possible price paths, and quantify the potential downside risk over a 1-month horizon accounting for market uncertainty.

---

## Features

- **Historical Data Processing:**  
  Loads historical closing price data and computes daily log returns.

- **Parameter Estimation:**  
  Estimates drift (μ) and volatility (σ) parameters for GBM from the log returns, annualized for simulation use.

- **Monte Carlo Simulation:**  
  Simulates multiple future price paths based on estimated parameters and GBM theory.

- **Risk Metrics Calculation:**  
  Calculates Value at Risk (VaR) and Expected Shortfall (ES) for typical confidence levels (95%, 99%) from simulated price paths.

- **Visualization:**

  - Plots sample simulated price paths showing potential future price ranges.
  - Plots histogram of simulated returns with VaR and ES clearly marked.

- **Reporting and Documentation:**  
  Designed for integration in a Jupyter notebook providing clear stepwise explanation, reproducibility, and interpretation of results.

---

## Getting Started

### Prerequisites

- Python 3.7+
- Libraries: `numpy`, `pandas`, `matplotlib`, `yfinance`

Install dependencies using:

```
pip install numpy pandas matplotlib yfinance
```

### Data

- The project uses historical stock data downloaded via `yfinance` or can be loaded from CSV files (`historicalData.csv`).

---

## Usage

1. **Load historical data** using data loader or directly from CSV.
2. **Compute log returns** and estimate annualized drift (μ) and volatility (σ).
3. **Run Monte Carlo simulations** of future price paths over desired horizon (e.g., 1 month).
4. **Calculate risk metrics** (VaR and ES) from simulations for specified confidence levels.
5. **Create visualizations** for price paths and return distributions.
6. **Interpret results** to understand downside risk levels.

---

## Interpretation of Risk Metrics

- **Value at Risk (VaR):** Maximum expected loss at a given confidence level (e.g., 95%, 99%).
- **Expected Shortfall (ES):** Average loss assuming the loss exceeds VaR, measuring tail risk severity.

These metrics help quantify potential losses to support risk management and investment decisions.

---

## Future Enhancements

- Portfolio-level risk simulation incorporating correlations.
- More advanced stochastic models (stochastic volatility, jumps).
- Integration with option pricing frameworks and Greeks estimation.
- Scenario analysis with shocks or regime changes.

---
