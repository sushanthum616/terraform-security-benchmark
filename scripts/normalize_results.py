#!/usr/bin/env python3
"""Normalize observed Checkov, Trivy, and KICS JSON into benchmark CSV."""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "normalized"
FIELDS = ["Case ID", "Scanner", "Scanner rule ID", "Reported title", "Severity",
          "File", "Resource", "Expected issue", "Detection classification",
          "Scan duration"]
CASE_EXPECTATIONS = {
    "case-01": "Public S3 access", "case-02": "No default S3 encryption",
    "case-03": "S3 versioning disabled", "case-04": "Unrestricted SSH port 22",
    "case-05": "Unrestricted RDP port 3389", "case-06": "Wildcard IAM permissions",
    "case-07": "Unencrypted EBS volume", "case-08": "Public RDS instance",
    "case-09": "Unencrypted RDS storage", "case-10": "CloudTrail validation disabled",
    "case-11": "CloudTrail without customer-managed KMS", "case-12": "KMS rotation disabled",
}
KEYWORDS = {
    "case-01": ("public", "principal", "bucket", "s3"),
    "case-02": ("encrypt", "encryption"),
    "case-03": ("version",),
    "case-04": ("ssh", "port 22", "22", "security group"),
    "case-05": ("rdp", "3389"),
    "case-06": ("iam", "privilege", "permission", "wildcard", "full"),
    "case-07": ("ebs", "volume", "encrypt"),
    "case-08": ("rds", "public"),
    "case-09": ("rds", "storage", "encrypt", "database"),
    "case-10": ("cloudtrail", "validation", "log"),
    "case-11": ("cloudtrail", "kms", "encrypt"),
    "case-12": ("kms", "rotation", "key"),
}

def case_from(path):
    match = re.search(r"(case-[0-9]{2})", str(path))
    return match.group(1) if match else ""

def classification(case_id, file_name, title):
    relevant = any(word in title.lower() for word in KEYWORDS.get(case_id, ()))
    vulnerable = "vulnerable.tf" in file_name.lower()
    if vulnerable and relevant:
        return "True positive"
    if not vulnerable and relevant:
        return "Possible false positive"
    return "Additional valid finding"

def duration(scanner):
    meta = OUT.parent / scanner / "scan-meta.txt"
    if not meta.exists():
        return ""
    text = meta.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"duration_seconds=([0-9.]+)", text)
    return match.group(1) if match else ""

def row(case_id, scanner, rule, title, severity, file_name, resource):
    return {
        "Case ID": case_id, "Scanner": scanner, "Scanner rule ID": rule,
        "Reported title": title, "Severity": severity or "",
        "File": file_name, "Resource": resource or "",
        "Expected issue": CASE_EXPECTATIONS.get(case_id, ""),
        "Detection classification": classification(case_id, file_name, title),
        "Scan duration": duration(scanner),
    }

def checkov_rows():
    data = json.loads((OUT.parent / "checkov" / "checkov-raw.json").read_text(encoding="utf-8-sig"))
    return [row(case_from(x.get("file_path", "")), "Checkov", x.get("check_id", ""),
                x.get("check_name", ""), x.get("severity"), x.get("file_path", ""),
                x.get("resource", ""))
            for x in data.get("results", {}).get("failed_checks", [])]

def trivy_rows():
    data = json.loads((OUT.parent / "trivy" / "all.json").read_text(encoding="utf-8-sig"))
    rows = []
    for result in data.get("Results", []):
        for x in result.get("Misconfigurations", []):
            rows.append(row(case_from(result.get("Target", "")), "Trivy",
                             x.get("ID", ""), x.get("Title", ""), x.get("Severity"),
                             result.get("Target", ""),
                             x.get("CauseMetadata", {}).get("Resource", "")))
    return rows

def kics_rows():
    data = json.loads((OUT.parent / "kics" / "results.json").read_text(encoding="utf-8-sig"))
    rows = []
    for query in data.get("queries", []):
        for x in query.get("files", []):
            rows.append(row(case_from(x.get("file_name", "")), "KICS",
                             query.get("query_id", ""), query.get("query_name", ""),
                             query.get("severity"), x.get("file_name", ""),
                             x.get("resource_type", "")))
    return rows

def main():
    rows = checkov_rows() + trivy_rows() + kics_rows()
    output = OUT / "normalized-findings.csv"
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} observed findings to {output}")

if __name__ == "__main__":
    main()

