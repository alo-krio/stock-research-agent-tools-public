# Compare portfolio construction methods

**Inputs.** Dated asset returns, eligibility, constraints and a feasible reference portfolio.

1. Estimate inputs on an earlier window and apply weights only after their calculation time.
2. Compare an equal-weight baseline with the candidate portfolio on identical assets. Track cash, concentration, exposures and turnover.
3. Stress missing histories, transaction costs and concentration limits. Record infeasible allocations explicitly.

**Acceptance check.** Reconcile weights and cash to total capital on every rebalance. Report the effect of constraints and costs separately from forecast quality.

**Upstream resources.** [skfolio](https://github.com/skfolio/skfolio) · [cvxportfolio](https://github.com/cvxgrp/cvxportfolio) · [PyPortfolioOpt](https://github.com/PyPortfolio/PyPortfolioOpt)
