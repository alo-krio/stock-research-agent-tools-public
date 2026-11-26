# Build a point-in-time equity panel

**Inputs.** A dated roster, OHLCV bars, filings and an exchange calendar.

1. Select the roster effective on each historical date. Track additions, removals, share classes and ticker changes under stable identifiers.
2. Separate the period a fact describes from the time it became public. Join each observation backward from the decision timestamp.
3. Generate expected sessions and reconcile missing bars, early closes and corporate actions. Keep a missing-data count for delisted securities.

**Acceptance check.** Add a synthetic amendment published after the decision date. The earlier panel should retain the original filing value. Record the release times, source versions and unmatched rows.

**Upstream resources.** [exchange_calendars](https://github.com/gerrymanoim/exchange_calendars) · [Historical S&P 500 constituents (fja05680)](https://github.com/fja05680/sp500) · [DuckDB](https://github.com/duckdb/duckdb)
