# Worklog

## Checklist

- [x] Inspect the workspace and define the local-only safety boundary.
- [x] Create the benchmark layout and three priority cases.
- [x] Create the remaining nine benchmark cases.
- [x] Add standards-mapped metadata and benchmark matrix.
- [x] Run Checkov, Trivy, and KICS where available.
- [x] Normalize scanner output after scans complete.
- [x] Run local static checks that do not contact AWS.
- [x] Review files for credentials, real identifiers, and prohibited commands.

## 2026-09-23

- Workspace was empty apart from the generated `work/` and `outputs/` directories.
- Available commands: Docker and Git. Terraform, Python, Checkov, Trivy, and KICS were not available on PATH.
- Created all 12 vulnerable/secure Terraform pairs and metadata files.
- Scanner execution is blocked until the tools are installed or supplied locally. No AWS command, API call, credential lookup, Terraform deployment command, or external upload was performed.

## 2026-10-01

- Started Docker Desktop and verified Docker client/daemon version 29.8.0.
- Downloaded pinned container images for Terraform 1.10.5, Checkov 3.3.22, Trivy 0.75.0, and KICS 2.1.20; image digests are recorded in docs/tool-versions.txt.
- Corrected invalid compressed HCL exposed by Terraform parsing, then confirmed terraform fmt -check -recursive passes.
- Checkov completed with exit status 1 and reported 139 passed / 153 failed checks; Trivy completed with exit status 0; KICS completed with exit status 60 because findings were detected.
- Preserved raw machine-readable output, human-readable transcripts, scan metadata, and KICS SARIF output.
- Normalized 420 observed findings and generated results/normalized/comparison-summary.md.
- No AWS command, API call, credential use, Terraform plan/apply/destroy/import/refresh, deployment, or external upload occurred.
- Isolated Terraform validation passed for the first vulnerable case, then provider installation stalled for subsequent isolated modules; this remains an explicit blocker.

## Evidence policy

Only commands actually run and outputs actually produced may be recorded as scanner evidence. Empty result files must not be treated as scan results.
