# Value-at-Risk-VaR-Calculator-for-BTCUSD
Bitcoin is one of the most volatile assets in the world, making it a great example to test risk models. The project compares how different VaR methods capture this risk, and whether assuming normality (parametric / Monte Carlo) underestimates tail risk compared to real market data (historical method).

Methods
1. Historical Simulation
Uses actual daily returns from BTC-USD. VaR is the empirical quantile of returns (e.g., 5% worst days).
2. Parametric (Variance–Covariance)
Assumes returns are normally distributed. VaR is computed using the mean, volatility, and normal distribution quantiles.
3. Monte Carlo Simulation
Generates thousands of random returns from a normal distribution with estimated mean & volatility. VaR is estimated from the simulated distribution.
