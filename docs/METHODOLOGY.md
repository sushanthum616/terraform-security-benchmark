# Methodology

1. Treat each case as one ground-truth issue. The vulnerable file contains the issue; the secure file changes only the relevant control.
2. Scan both files with each available scanner using Terraform/configuration-only modes and record command, version, timestamp, duration, and exit status.
3. Preserve raw JSON/SARIF/text output under `results/<scanner>/`.
4. Normalize only observed findings. A missing finding on a vulnerable file is a false negative for the benchmark issue; a finding on the corrected file is a possible false positive until manually reviewed.
5. Do not infer false positives from rule names alone. Record reasoning in `docs/benchmark-matrix.csv` or the worklog.

Standards references used for mappings are MITRE CWE definitions and AWS documentation for CIS AWS Foundations control applicability. The CIS control label is version-qualified where possible; scanner rule identifiers are recorded only after actual testing.
