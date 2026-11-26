# Give a research agent read-only tools

**Inputs.** A local catalog, an operator-approved list of data operations and a synthetic input.

1. Use the offline registry search to identify candidate resources. Inspect each project's actual API and permissions before integration.
2. Expose only the data-reading functions needed for the experiment. Keep credentials in the host's secret store and use fixtures for all execution simulations.
3. Enumerate the tools visible to the agent and run one bounded read. Verify that order submission, cancellation, withdrawals and arbitrary command execution are absent.

**Acceptance check.** Record the exposed tool names, versions and expected output for the fixture. Repeat the check after dependency or permission changes.

**Upstream resources.** [Pydantic AI](https://github.com/pydantic/pydantic-ai) · [alpaca-py (market data + paper)](https://github.com/alpacahq/alpaca-py) · [SEC EDGAR APIs (submissions, companyfacts, frames)](https://www.sec.gov/search-filings/edgar-application-programming-interfaces)
