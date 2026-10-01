terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

variable "benchmark_password" {
  type      = string
  sensitive = true
}
resource "aws_db_instance" "benchmark" {
  identifier          = "benchmark-fictional-private-db"
  engine              = "postgres"
  instance_class      = "db.t3.micro"
  allocated_storage   = 20
  username            = "benchmark_user"
  password            = var.benchmark_password
  publicly_accessible = false
  skip_final_snapshot = true
}

