# Comparison summary

Generated from observed scanner output. Findings on corrected files are retained as possible false positives or additional valid findings.

| Metric | Checkov | Trivy | KICS |
|---|---:|---:|---:|
| Detection rate | 100.0% | 75.0% | 83.3% |
| Missed benchmark cases | none | case-02, case-03, case-06 | case-02, case-05 |
| True-positive cases | 12 | 9 | 10 |
| Additional valid findings | 58 | 62 | 80 |
| Scan duration seconds | 0.1984247 | 8.0756828 | 30.2972673 |
| Remediation guidance | Present in observed rule output | Present in observed rule output | Present in observed rule output |

Tool-exclusive and overlap sets are based on benchmark cases classified as true positives:
- Checkov only: ['case-02']
- Trivy only: none
- KICS only: none
- All three: ['case-01', 'case-04', 'case-07', 'case-08', 'case-09', 'case-10', 'case-11', 'case-12']

Classification is heuristic and must be manually reviewed before publication; scanner-specific additional findings are not treated as benchmark misses.
