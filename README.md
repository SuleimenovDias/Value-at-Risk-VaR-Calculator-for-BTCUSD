# Value-at-Risk-VaR-Calculator-for-BTCUSD
Bitcoin is one of the most volatile assets in the world, making it a great example to test risk models. The project compares how different VaR methods capture this risk, and whether assuming normality (parametric / Monte Carlo) underestimates tail risk compared to real market data (historical method).

Methods
1. Historical Simulation
Uses actual daily returns from BTC-USD. VaR is the empirical quantile of returns (e.g., 5% worst days).
2. Parametric (Variance–Covariance)
Assumes returns are normally distributed. VaR is computed using the mean, volatility, and normal distribution quantiles.
3. Monte Carlo Simulation
Generates thousands of random returns from a normal distribution with estimated mean & volatility. VaR is estimated from the simulated distribution.

| Method      | VaR 5%  | VaR 1%  |
| ----------- | ------- | ------- |
| Historical  | -0.0501 | -0.0873 |
| Parametric  | -0.0532 | -0.0761 |
| Monte Carlo | -0.0531 | -0.0756 |

Observations

5% VaR
Parametric and Monte Carlo are slightly more negative than Historical. Historical 5% VaR is slightly smaller — this is because BTC returns have heavy tails, so the lower 5% of actual returns includes some extreme negative days.

1% VaR
Historical VaR is more negative than Parametric/Monte Carlo. This is expected: the extreme 1% of daily BTC returns includes rare huge drops (fat tails) that the normal assumption underestimates. Parametric & Monte Carlo, which rely on normality, underestimate the worst-case tail risk.
