import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

btc = yf.download("BTC-USD", start="2020-01-01", end="2025-01-01")

btc = btc[["Close"]].rename(columns={"Close": "Price"})

btc["Return"] = btc["Price"].pct_change().dropna()

VaR_5 = np.percentile(btc["Return"].dropna(), 5)
VaR_1 = np.percentile(btc["Return"].dropna(), 1)

print(f"5% Historical VaR: {VaR_5:.4f}")
print(f"1% Historical VaR: {VaR_1:.4f}")
