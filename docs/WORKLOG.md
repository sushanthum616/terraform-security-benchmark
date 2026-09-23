# Worklog

## Checklist

- [x] Inspect the workspace and define the local-only safety boundary.
- [x] Create the benchmark layout and three priority cases.
- [x] Create the remaining nine benchmark cases.
- [x] Add standards-mapped metadata and benchmark matrix.
- [ ] Run Checkov, Trivy, and KICS where available.
- [ ] Normalize scanner output after scans complete.
- [x] Run local static checks that do not contact AWS.
- [x] Review files for credentials, real identifiers, and prohibited commands.

## 2026-09-23

- Workspace was empty apart from the generated `work/` and `outputs/` directories.
- Available commands: Docker and Git. Terraform, Python, Checkov, Trivy, and KICS were not available on PATH.
- Created all 12 vulnerable/secure Terraform pairs and metadata files.
- Scanner execution is blocked until the tools are installed or supplied locally. No AWS command, API call, credential lookup, Terraform deployment command, or external upload was performed.

## Evidence policy

Only commands actually run and outputs actually produced may be recorded as scanner evidence. Empty result files must not be treated as scan results.
