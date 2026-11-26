# Report results against a benchmark

**Inputs.** A dated equity curve, benchmark return series, fills and declared transaction costs.

1. Align currency, sessions and return conventions. Document dividend treatment and the handling of idle cash.
2. Reconstruct the equity curve from the ledger. Compute drawdown, turnover and gross and net returns on the same evaluation interval.
3. Break out exposure to broad market moves where the data support it. Report the number of observations and sensitivity to start date.

**Acceptance check.** Include a reproducible input version and explain any difference between the ledger and the report. Label synthetic and historical results distinctly.

**Upstream resources.** [QuantStats](https://github.com/ranaroussi/quantstats) · [empyrical-reloaded](https://github.com/stefan-jansen/empyrical-reloaded) · [Kenneth French Data Library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html)
