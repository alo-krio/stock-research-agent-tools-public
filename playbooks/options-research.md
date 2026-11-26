# Interpret option-implied observations

**Inputs.** Timestamped bid/ask quotes, strikes, expirations, underlying price and contract terms.

1. Align the underlying price and option quote in time. Identify American or European exercise, dividends and corporate-action adjustments.
2. Check bid/ask ordering, stale quotes and contract multipliers. Compute model outputs using documented rate and dividend assumptions.
3. Compare adjacent strikes and expirations. Recalculate using each side of the spread to show sensitivity to the input price.

**Acceptance check.** Test the calculation on a synthetic quote with a known model price. Flag nonconvergence and impossible prices instead of treating them as observations.

**Upstream resources.** [QuantLib (+ QuantLib-SWIG Python)](https://github.com/lballabio/QuantLib) · [FinancePy](https://github.com/FinancePy-Org/FinancePy) · [Cboe options market statistics](https://www.cboe.com/us/options/market_statistics/)
