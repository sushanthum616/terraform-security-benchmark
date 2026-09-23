terraform { required_providers { aws = { source = "hashicorp/aws", version = "~> 5.0" } } }
provider "aws" { region = "us-east-1" }
resource "aws_s3_bucket" "logs" { bucket = "benchmark-fictional-trail-kms" }
resource "aws_kms_key" "logs" { description = "Fictional benchmark log key"; enable_key_rotation = true }
resource "aws_cloudtrail" "benchmark" { name = "benchmark-fictional-kms"; s3_bucket_name = aws_s3_bucket.logs.id; kms_key_id = aws_kms_key.logs.arn; include_global_service_events = true; is_multi_region_trail = false }
