# Test a proposed signal

**Inputs.** A precisely specified signal, a historical universe and a benchmark.

1. Write down the information cutoff, first possible entry, exit and expected direction before computing returns.
2. Compute the signal with trailing observations. Evaluate forward outcomes from the first feasible fill. Separate overlapping windows or report their dependence.
3. Compare the same issuers and dates with a passive control. Repeat with a delayed fill and greater transaction costs.

**Acceptance check.** Show the number of independent events, skipped observations and the result of changing execution assumptions. Reserve fresh dates before choosing among variants.

**Upstream resources.** [backtesting.py](https://github.com/kernc/backtesting.py) · [alphalens-reloaded](https://github.com/stefan-jansen/alphalens-reloaded)
