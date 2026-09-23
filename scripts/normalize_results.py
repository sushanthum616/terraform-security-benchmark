#!/usr/bin/env python3
"""Normalize observed scanner JSON into a common CSV.

This script intentionally emits no fabricated findings. It accepts a manifest
of observed findings and the benchmark matrix; scanner adapters can be added
without changing the output schema.
"""
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "results" / "normalized" / "observed-findings.json"
OUTPUT = ROOT / "results" / "normalized" / "normalized-findings.csv"
FIELDS = ["Case ID", "Scanner", "Scanner rule ID", "Reported title", "Severity", "File", "Resource", "Expected issue", "Detection classification", "Scan duration"]

def main():
    observations = []
    if INPUT.exists():
        observations = json.loads(INPUT.read_text(encoding="utf-8"))
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        for item in observations:
            writer.writerow({field: item.get(field, "") for field in FIELDS})
    print(f"Wrote {len(observations)} observed findings to {OUTPUT}")

if __name__ == "__main__":
    main()
