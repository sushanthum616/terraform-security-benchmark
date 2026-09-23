terraform { required_providers { aws = { source = "hashicorp/aws", version = "~> 5.0" } } }
provider "aws" { region = "us-east-1" }
resource "aws_s3_bucket" "benchmark" { bucket = "benchmark-fictional-public-access" }
resource "aws_s3_bucket_policy" "benchmark" {
  bucket = aws_s3_bucket.benchmark.id
  policy = jsonencode({ Version = "2012-10-17", Statement = [{ Effect = "Allow", Principal = "*", Action = "s3:GetObject", Resource = "${aws_s3_bucket.benchmark.arn}/*" }] })
}
