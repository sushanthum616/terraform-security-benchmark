terraform { required_providers { aws = { source = "hashicorp/aws", version = "~> 5.0" } } }
provider "aws" { region = "us-east-1" }
resource "aws_security_group" "benchmark" { name = "benchmark-fictional-restricted-rdp"; description = "Benchmark only"; ingress { from_port = 3389; to_port = 3389; protocol = "tcp"; cidr_blocks = ["198.51.100.0/24"] } }
