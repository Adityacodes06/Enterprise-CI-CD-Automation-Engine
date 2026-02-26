variable "aws_region" {
  description = "AWS region for resources"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Environment name (e.g., dev, staging, prod)"
  type        = string
  default     = "dev"
}

variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "availability_zones" {
  description = "List of availability zones for multi-AZ deployment"
  type        = list(string)
}

variable "app_node_count" {
  description = "Number of application nodes to provision"
  type        = number
  default     = 3
}

variable "instance_type" {
  description = "EC2 instance type for app nodes"
  type        = string
  default     = "t3.micro"
}

variable "project_name" {
  description = "Project name for resource naming"
  type        = string
  default     = "cicd-automation"
}
