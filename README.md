# Stock Research Agent Tools

A curated directory of **278 resources across 24 categories** for U.S. equity research, backtesting and agent evaluation. Browse the [resource directory](registry/README.md), choose one of the [12 research playbooks](playbooks/README.md), or filter tools using the [dated verification results](verification/README.md).

## Search locally

Use Python 3.8 or later from the checkout. Search reads two bundled JSON files and requires no package installation, network connection or API keys.

```sh
python3 scripts/search.py "backtesting" --outcome pass --limit 5
python3 scripts/search.py --category "filings" --limit 8
python3 scripts/search.py duckdb --json
```

All terms must match the resource ID, name, purpose or category. The category filter accepts substrings; kind and outcome filters use exact values. Results retain directory order. Each JSON result includes its upstream URL, intended use and available check records.

## Where to start

- **Historical equity data.** Pair an exchange calendar with dated membership and an as-of join. Verify that a later filing amendment cannot leak into an earlier decision. [Point-in-time panel](playbooks/point-in-time-data.md)
- **Strategy evaluation.** Compare a hand-calculated ledger against two engines before trying parameter sweeps. [Engine reconciliation](playbooks/engine-parity.md)
- **Agent research.** Freeze the evidence packet and check citations, numerical accuracy and abstentions. [Agent evaluation](playbooks/agent-evaluation.md)

## Scope and reuse

The directory includes open-source libraries, research papers, models, public datasets, commercial services, and historical projects. A listing is a discovery lead. Check the upstream project for current maintenance, licensing, market coverage, API costs and data redistribution rights. Historical smoke tests cover a limited operation in a particular environment. They do not establish trading performance.

The search tool only reads local files. No third-party software, model weights, financial datasets, credentials or broker connections are required to browse this project. The [MIT license](LICENSE) applies to the original code, documentation and compilation in this repository. Linked projects and data retain their own terms.
