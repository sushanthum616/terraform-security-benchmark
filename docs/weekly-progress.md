# Weekly progress

## Findings this week

- Docker Desktop was started and its local daemon became available.
- Pinned Terraform, Checkov, Trivy, and KICS containers were downloaded and their versions and digests recorded.
- Terraform formatting passed for all benchmark files.
- Checkov, Trivy, and KICS scanned the complete benchmark tree. Raw JSON/SARIF and human-readable transcripts were preserved.
- The normalization script produced 420 observed findings and the comparison summary was generated from those findings.
- Validation exposed and corrected invalid HCL compression in the original files. Isolated validation successfully passed for the first vulnerable case; repeated provider installation then stalled for the remaining isolated modules.

## Improvements over the previous week

- The benchmark is now scanner-executable rather than only source-complete.
- Scanner evidence is versioned by tool version, image digest, exit status, and duration.
- Findings are normalized into one CSV schema with benchmark-case classifications.
- Additional scanner findings are kept separate from benchmark true positives.

## Plan for next week

- Complete isolated Terraform validation using a persistent provider cache or host Terraform installation.
- Manually review classifier matches, especially possible false positives and additional valid findings.
- Refine benchmark examples where scanner parsing or case isolation affects interpretation.
- Commit the corrected Terraform and evidence updates and push the next research snapshot.

