terraform { required_providers { aws = { source = "hashicorp/aws", version = "~> 5.0" } } }
provider "aws" { region = "us-east-1" }
resource "aws_s3_bucket" "benchmark" { bucket = "benchmark-fictional-encrypted" }
resource "aws_s3_bucket_server_side_encryption_configuration" "benchmark" { bucket = aws_s3_bucket.benchmark.id; rule { apply_server_side_encryption_by_default { sse_algorithm = "AES256" } } }
