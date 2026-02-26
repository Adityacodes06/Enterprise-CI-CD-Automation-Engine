#!/bin/bash
set -e

# Install Docker (for containerized deployments)
yum update -y
yum install -y docker
systemctl start docker
systemctl enable docker
usermod -aG docker ec2-user

# Install Python 3.11
yum install -y python3.11 python3.11-pip
alternatives --set python3 /usr/bin/python3.11

# Create app directory
mkdir -p /opt/app
chown ec2-user:ec2-user /opt/app
