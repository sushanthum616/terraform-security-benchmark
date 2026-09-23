terraform { required_providers { aws = { source = "hashicorp/aws", version = "~> 5.0" } } }
provider "aws" { region = "us-east-1" }
resource "aws_ebs_volume" "benchmark" { availability_zone = "us-east-1a"; size = 20; encrypted = true; tags = { Name = "benchmark-fictional-ebs" } }
