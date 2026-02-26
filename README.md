# Enterprise CI/CD Automation Engine

Infrastructure-as-Code automation using **Terraform** to provision multi-node VPC environments on AWS, with **Jenkins** pipelines for build, test, and blue-green deployment workflows.

## Tech Stack

- **Python 3.9+** – Application and automation logic
- **Terraform** – Infrastructure as Code (AWS VPC, EC2, networking)
- **Jenkins** – CI/CD pipelines
- **AWS** – Cloud infrastructure

## Project Structure

```
.
├── app/                    # Python application
│   ├── src/app/            # Application source
│   │   ├── main.py         # Main orchestration
│   │   ├── api/            # API routes
│   │   └── services/       # Deployer, health check
│   ├── tests/              # Unit tests (95% coverage target)
│   ├── requirements.txt
│   ├── setup.py
│   └── Dockerfile
├── terraform/              # IaC - multi-node VPC
│   ├── main.tf             # VPC, subnets, NAT, routing
│   ├── ec2.tf              # App nodes, security groups
│   ├── variables.tf
│   ├── outputs.tf
│   └── terraform.tfvars.example
├── jenkins/
│   ├── Jenkinsfile         # Build, test, blue-green deploy
│   └── blue-green.Jenkinsfile
├── scripts/
│   └── blue-green-deploy.sh
└── README.md
```

## Prerequisites

- Python 3.9+
- Terraform >= 1.0
- AWS CLI configured
- Jenkins (for CI/CD)
- Docker (for containerized deployments)

## Quick Start

### 1. Terraform (Infrastructure)

```bash
cd terraform

# Copy and edit variables
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with your AWS region and availability zones

# Initialize and apply
terraform init
terraform plan
terraform apply
```

### 2. Python Application

```bash
cd app

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # Linux/macOS

# Install dependencies
pip install -e .
pip install -r requirements.txt

# Run tests (95% coverage required)
pytest tests/ -v --cov=src --cov-report=term --cov-fail-under=95
```

### 3. Jenkins Pipeline

1. Create a Pipeline job in Jenkins
2. Point it to your repository
3. Use `jenkins/Jenkinsfile` as the Pipeline script
4. Configure credentials: `docker-registry-credentials` for Docker registry
5. Ensure Jenkins has AWS credentials for deployment

**Pipeline stages:**
- Checkout
- Build
- Unit Tests (95% coverage gate)
- Package
- Build Docker Image (main branch)
- Blue-Green Deployment (main branch)

### 4. Blue-Green Deployment Script

The `scripts/blue-green-deploy.sh` script supports:

```bash
# Initial deploy (from Jenkins)
./blue-green-deploy.sh <workspace> <app_name> <image_tag>

# Promote environment
./blue-green-deploy.sh promote blue|green <image_tag>
```

## Features

- **Multi-node VPC** – Private/public subnets across multiple AZs
- **EC2 App Nodes** – Configurable count, spread across AZs
- **Unit Testing** – 95% code coverage before production
- **Blue-Green Deployments** – Zero-downtime deployments
- **Jenkins Automation** – Build, test, package, deploy

## Outputs (Terraform)

After `terraform apply`:

| Output            | Description                    |
|-------------------|--------------------------------|
| `vpc_id`          | Provisioned VPC ID             |
| `public_subnet_ids` | Public subnet IDs           |
| `private_subnet_ids` | Private subnet IDs          |
| `app_instance_ids`  | EC2 instance IDs             |
| `app_instance_private_ips` | Node private IPs       |

## License

MIT
