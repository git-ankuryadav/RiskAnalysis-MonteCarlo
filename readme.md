# Monte Carlo Simulation for Risk Analysis on Indian Stocks

This project performs quantitative risk analysis on Indian stock prices using Monte Carlo simulations based on Geometric Brownian Motion (GBM) and Jump Diffusion models. It estimates potential future price scenarios and downside risk metrics like Value at Risk (VaR) and Expected Shortfall (ES) over a specified time horizon, accounting for both continuous price movements and rare jumps.

---

## Project Overview

The goal is to model possible future price movements of an Indian stock (e.g., COAL INDIA) using historical price data, simulate many possible price paths, and quantify the potential downside risk over a 1-month horizon accounting for market uncertainty, including extreme market moves.

---

## Features

- **Historical Data Processing:**  
  Loads historical closing price data and computes daily log returns.

- **Parameter Estimation:**  
  Estimates drift (μ) and volatility (σ) parameters for GBM from the log returns, annualized for simulation use.  
  Estimates jump diffusion parameters including jump intensity (λ), mean jump size (μ_J), and jump volatility (σ_J) by detecting jumps in log returns.

- **Monte Carlo Simulation:**  
  Simulates multiple future price paths based on estimated parameters using both:

  - Geometric Brownian Motion (GBM)
  - Jump Diffusion model incorporating random jumps to capture fat tails and sudden price changes.

- **Risk Metrics Calculation:**  
  Calculates Value at Risk (VaR) and Expected Shortfall (ES) for typical confidence levels (95%, 99%) from simulated price paths.

- **Validation and Backtesting:**  
  Compares simulated risk metrics to historical rolling 30-day return extremes for model validation.

- **Visualization:**

  - Plots sample simulated price paths showing potential future price ranges.
  - Plots histogram of simulated returns with VaR and ES clearly marked.
  - Diagnostic plots for assessing GBM assumptions: ACF of log returns, histogram, Q-Q plot.

---

## Getting Started

### Prerequisites

- Python 3.7+
- Libraries: `numpy`, `pandas`, `matplotlib`, `yfinance`, `scipy`, `statsmodels`

Install dependencies using:

```
pip install numpy pandas matplotlib yfinance scipy statsmodels

```

### Data

- The project uses historical stock data downloaded via `yfinance` or can be loaded from CSV files (`historicalData.csv`).

---

## Usage

1. **Load historical data** using data loader or directly from CSV.
2. **Compute log returns** and perform statistical checks for GBM assumptions (normality, independence, stationarity).
3. **Estimate GBM parameters (μ, σ) and Jump Diffusion parameters (λ, μ_J, σ_J)** from the data.
4. **Run Monte Carlo simulations** of future price paths using GBM or Jump Diffusion over the desired horizon (e.g., 1 month).
5. **Calculate risk metrics** (VaR and ES) from simulations on specified confidence levels.
6. **Validate by comparing to actual historical 30-day return extremes.**
7. **Create visualizations** for price paths, return histograms, and diagnostic plots.
8. **Interpret results** to understand downside risk and model fit.

---

## Interpretation of Risk Metrics

- **Value at Risk (VaR):** Maximum expected loss at a given confidence level (e.g., 95%, 99%).
- **Expected Shortfall (ES):** Average loss assuming the loss exceeds VaR, measuring tail risk severity.
- **Historical Comparison:** Comparing Monte Carlo VaR/ES to actual extreme historical losses helps validate model realism and tail risk capture.

These metrics help quantify potential losses to support risk management and investment decisions, especially under jump diffusion capturing rare shocks missed by GBM alone.

---

## Diagnostic Results for GBM Assumptions

- Stationarity confirmed by Augmented Dickey-Fuller test (p < 0.001).
- Empirical log returns exhibit approximate normality with slight tail deviations (Shapiro-Wilk normality test rejects normality at 5%).
- Log returns show minimal autocorrelation based on ACF plots, satisfying GBM independence assumption.

These diagnostics justify the use of GBM as a baseline model while motivating the jump diffusion model for tail behavior.

---

This project balances mathematical modeling, statistical validation, and practical risk metrics to provide robust risk analysis of Indian equities, extendable to complex financial instruments.
