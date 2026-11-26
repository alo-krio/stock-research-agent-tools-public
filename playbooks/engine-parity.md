# Reconcile two backtests

**Inputs.** A short synthetic price path with known targets, fees and a cash balance.

1. Hand-calculate fills, shares, fees, cash and equity for a single round trip.
2. Run the same targets in two engines using the same fill time, position sizing and fee convention. Inspect the first divergent ledger row.
3. Add one complication at a time, such as a gap, fractional share or open position at the last observation.

**Acceptance check.** Save the reconciled ledger and exact configurations. Matching final returns alone can hide offsetting fill and accounting errors.

**Upstream resources.** [bt](https://github.com/pmorissette/bt) · [backtesting.py](https://github.com/kernc/backtesting.py)
