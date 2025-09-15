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

print(f"Mean daily return: {mu:.4%}")
print(f"Volatility (std): {sigma:.4%}")

z_5 = norm.ppf(0.05)
z_1 = norm.ppf(0.01)

print(f"Z (5%): {z_5:.3f}, Z (1%): {z_1:.3f}")

VaR_5_param = mu + z_5 * sigma
VaR_1_param = mu + z_1 * sigma

print(f"5% Parametric VaR: {VaR_5_param:.4f}")
print(f"1% Parametric VaR: {VaR_1_param:.4f}")
