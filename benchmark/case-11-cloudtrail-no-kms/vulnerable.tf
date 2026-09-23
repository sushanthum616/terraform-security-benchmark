terraform { required_providers { aws = { source = "hashicorp/aws", version = "~> 5.0" } } }
provider "aws" { region = "us-east-1" }
resource "aws_s3_bucket" "logs" { bucket = "benchmark-fictional-trail-no-kms" }
resource "aws_cloudtrail" "benchmark" { name = "benchmark-fictional-no-kms"; s3_bucket_name = aws_s3_bucket.logs.id; include_global_service_events = true; is_multi_region_trail = false }
