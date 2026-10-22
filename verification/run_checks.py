#!/usr/bin/env python3
"""Run the deterministic finite checks and write their machine-readable result."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import cache_checks
import matrix_checks


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent / "results.json",
        help="Path for the JSON result (default: verification/results.json).",
    )
    args = parser.parse_args()
    result = {
        "schema_version": 1,
        "status": "passed",
        "scope": (
            "Finite-dimensional matrix identities and exhaustive finite cache experiments; "
            "these checks accompany the analytic proofs and do not establish asymptotic "
            "bounds, source-design construction, or hardware noise performance."
        ),
        "matrix_checks": matrix_checks.run(),
        "cache_checks": cache_checks.run(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("Passed: posterior identities, complete SWAP instrument, ancilla circuit,")
    print("local-measurement counterexample, and exact cache enumeration.")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
