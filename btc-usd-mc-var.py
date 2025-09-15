import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

btc = yf.download("BTC-USD", start="2020-01-01", end="2025-01-01")

btc = btc[["Close"]].rename(columns={"Close": "Price"})

btc["Return"] = btc["Price"].pct_change().dropna()

mu = btc["Return"].mean()
sigma = btc["Return"].std()

n_sim = 100000
simulated_returns = np.random.normal(mu, sigma, n_sim)

VaR_5_mc = np.percentile(simulated_returns, 5)
VaR_1_mc = np.percentile(simulated_returns, 1)

print(f"5% Monte Carlo VaR: {VaR_5_mc:.4f}")
print(f"1% Monte Carlo VaR: {VaR_1_mc:.4f}")

plt.figure(figsize=(10,5))
plt.hist(simulated_returns, bins=100, color="lightblue", edgecolor="black", alpha=0.7)
plt.axvline(VaR_5_mc, color="red", linestyle="--", label=f"VaR 5%: {VaR_5_mc:.2%}")
plt.axvline(VaR_1_mc, color="darkred", linestyle="--", label=f"VaR 1%: {VaR_1_mc:.2%}")
plt.title("Monte Carlo Simulation of BTC Returns")
plt.legend()
plt.show()