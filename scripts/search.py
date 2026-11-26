"""Search the local resource directory and its dated verification records."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def search(terms=(), category="", kind="", outcome="", limit=20):
    resources = json.loads((ROOT / "registry/resources.json").read_text(encoding="utf-8"))
    by_id = {}
    for check in json.loads((ROOT / "verification/results.json").read_text(encoding="utf-8")):
        by_id.setdefault(check["id"], []).append(check)
    matches = []
    for item in resources:
        checks = by_id.get(item["id"], [])
        if category.casefold() not in item["category"].casefold():
            continue
        if kind and kind.casefold() != item["kind"].casefold():
            continue
        if outcome and not any(c["outcome"] == outcome for c in checks):
            continue
        words = " ".join(item[k] for k in ("id", "name", "use", "category")).casefold()
        if all(term.casefold() in words for term in terms):
            matches.append({**item, "checks": checks})
    return {"total": len(matches), "results": matches[:limit]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("terms", nargs="*", help="Literal substrings; all must match")
    parser.add_argument("--category", default="", help="Substring of category name")
    parser.add_argument("--kind", default="", help="Exact artifact kind")
    parser.add_argument("--outcome", default="", help="Exact historical check outcome")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.limit < 0:
        parser.error("--limit must be nonnegative")
    result = search(args.terms, args.category, args.kind, args.outcome, args.limit)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"{result['total']} matches")
        for row in result["results"]:
            outcomes = ", ".join(c["outcome"] for c in row["checks"]) or "unverified"
            print(f"{row['id']} [{outcomes}]  {row['name']}\n  {row['use']}\n  {row['url']}")


if __name__ == "__main__":
    main()
