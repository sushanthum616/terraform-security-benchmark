#!/usr/bin/env python3
"""Build a factual comparison summary from normalized observed findings."""
import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
rows = list(csv.DictReader((ROOT / "results/normalized/normalized-findings.csv").open(encoding="utf-8")))
scanners = ["Checkov", "Trivy", "KICS"]
cases = [f"case-{i:02d}" for i in range(1, 13)]
true = defaultdict(set)
for row in rows:
    if row["Detection classification"] == "True positive":
        true[row["Scanner"]].add(row["Case ID"])
durations = {}
for scanner in scanners:
    meta = ROOT / "results" / scanner.lower() / "scan-meta.txt"
    text = meta.read_text(encoding="utf-8", errors="replace") if meta.exists() else ""
    durations[scanner] = next((line.split("=", 1)[1] for line in text.splitlines() if line.startswith("duration_seconds=")), "not recorded")
all_cases = set().union(*(true[s] for s in scanners))
lines = ["# Comparison summary", "", "This summary is generated from observed scanner output and the benchmark ground truth classifier.", "",
         "| Metric | Checkov | Trivy | KICS |", "|---|---:|---:|---:|"]
for scanner in scanners:
    rate = len(true[scanner]) / len(cases) * 100
    missed = ", ".join(sorted(set(cases) - true[scanner])) or "none"
    lines.append(f"| Detection rate | {rate:.1f}% | " if scanner == "Checkov" else "")
lines = ["# Comparison summary", "", "Generated from observed scanner output. Findings on corrected files are retained as possible false positives or additional valid findings.", "",
         "| Metric | Checkov | Trivy | KICS |", "|---|---:|---:|---:|",
         f"| Detection rate | {len(true['Checkov'])/12:.1%} | {len(true['Trivy'])/12:.1%} | {len(true['KICS'])/12:.1%} |",
         f"| Missed benchmark cases | {', '.join(sorted(set(cases)-true['Checkov'])) or 'none'} | {', '.join(sorted(set(cases)-true['Trivy'])) or 'none'} | {', '.join(sorted(set(cases)-true['KICS'])) or 'none'} |",
         f"| True-positive cases | {len(true['Checkov'])} | {len(true['Trivy'])} | {len(true['KICS'])} |",
         f"| Additional valid findings | {sum(r['Scanner']=='Checkov' and r['Detection classification']=='Additional valid finding' for r in rows)} | {sum(r['Scanner']=='Trivy' and r['Detection classification']=='Additional valid finding' for r in rows)} | {sum(r['Scanner']=='KICS' and r['Detection classification']=='Additional valid finding' for r in rows)} |",
         f"| Scan duration seconds | {durations['Checkov']} | {durations['Trivy']} | {durations['KICS']} |",
         "| Remediation guidance | Present in observed rule output | Present in observed rule output | Present in observed rule output |",
         "", "Tool-exclusive and overlap sets are based on benchmark cases classified as true positives:",
         f"- Checkov only: {sorted(true['Checkov'] - true['Trivy'] - true['KICS']) or 'none'}",
         f"- Trivy only: {sorted(true['Trivy'] - true['Checkov'] - true['KICS']) or 'none'}",
         f"- KICS only: {sorted(true['KICS'] - true['Checkov'] - true['Trivy']) or 'none'}",
         f"- All three: {sorted(true['Checkov'] & true['Trivy'] & true['KICS']) or 'none'}",
         "", "Classification is heuristic and must be manually reviewed before publication; scanner-specific additional findings are not treated as benchmark misses."]
(ROOT / "results/normalized/comparison-summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("Updated comparison summary")

