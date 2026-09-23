terraform { required_providers { aws = { source = "hashicorp/aws", version = "~> 5.0" } } }
provider "aws" { region = "us-east-1" }
resource "aws_kms_key" "benchmark" { description = "Fictional benchmark key"; enable_key_rotation = true }
