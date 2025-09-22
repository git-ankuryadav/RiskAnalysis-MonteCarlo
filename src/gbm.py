import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller

df2 = pd.read_csv("../data/historicalData.csv")
df = df2
df['Close'] = df2['Closing_Price']
df['Log_Return'] = np.log(df['Close'] / df['Close'].shift(1))
log_returns = df['Log_Return'].dropna()

# Histogram + Q-Q plot (requires statsmodels)
plt.hist(log_returns, bins=50, density=True, alpha=0.6)
plt.title("Histogram of Log Returns")
plt.savefig("../plots/hist-gbmtest.png")

import statsmodels.api as sm
sm.qqplot(log_returns, line='s')
plt.title("Q-Q Plot of Log Returns")
plt.savefig("../plots/qq-gbm.png")

# Normality test
stat, p = shapiro(log_returns)
print(f"Shapiro-Wilk test p-value: {p:.4f}")

# Autocorrelation
plot_acf(log_returns, lags=20)
plt.title("ACF of Log Returns")
plt.savefig("../plots/acf-logreturn.png")


# Stationarity test (ADF)
adf_result = adfuller(log_returns)
print(f"ADF Statistic: {adf_result[0]:.4f}, p-value: {adf_result[1]:.4f}")
