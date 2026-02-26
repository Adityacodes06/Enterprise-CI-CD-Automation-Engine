output "vpc_id" {
  description = "ID of the provisioned VPC"
  value       = aws_vpc.main.id
}

output "public_subnet_ids" {
  description = "IDs of public subnets"
  value       = aws_subnet.public[*].id
}

output "private_subnet_ids" {
  description = "IDs of private subnets"
  value       = aws_subnet.private[*].id
}

output "app_instance_ids" {
  description = "IDs of application EC2 instances"
  value       = aws_instance.app[*].id
}

output "app_instance_private_ips" {
  description = "Private IPs of application nodes"
  value       = aws_instance.app[*].private_ip
}
