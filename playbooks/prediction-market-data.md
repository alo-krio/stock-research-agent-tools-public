# Use prediction-market observations in research

**Inputs.** A dated quote, contract resolution rules and an independently identified event.

1. Match the contract wording, deadline and settlement criteria to the research question.
2. Record bid, ask, observation time and any available liquidity indicators. Identify stale or one-sided quotes.
3. Evaluate a frozen probability against the resolved event. Compare its calibration with a baseline across similarly defined contracts.

**Acceptance check.** Keep a mismatch log for ambiguous contracts. Use public market-data reads and saved observations; this procedure needs no wallet or order permissions.

**Upstream resources.** [pmxt unified prediction-market API](https://github.com/pmxt-dev/pmxt) · [Kalshi API](https://docs.kalshi.com/)
