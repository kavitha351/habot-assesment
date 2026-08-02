# Habot Hiring Project

## Junior Cloud & DevOps Engineer Assessment

**Candidate:** Kavitha Kumari

**Email:** kavithakumari351@gmail.com

**GitHub:** https://github.com/kavitha351/habot-assesment.git

---

## Project Overview

![Terraform](https://img.shields.io/badge/Terraform-IaC-blue)
![GitHub Actions](https://img.shields.io/badge/CI/CD-GitHub%20Actions-success)
![Python](https://img.shields.io/badge/Python-Django-blue)
![License](https://img.shields.io/badge/License-MIT-green)

This project demonstrates the implementation of a secure cloud infrastructure and automated quality assurance pipeline for a student onboarding system.

The solution includes:

- Infrastructure provisioning using Terraform
- Google Cloud Storage and BigQuery resources
- IAM configuration following the Principle of Least Privilege
- Automated CI/CD pipeline using GitHub Actions
- Django REST Framework serializer for strict request validation

The objective is to ensure secure infrastructure provisioning, automated code quality checks, and reliable data validation.

## Architecture

```

Student Onboarding Form

↓

Django REST API

↓

Google Cloud Storage (Raw Landing)

↓

BigQuery Dataset (Validated Data)

↓

Analytics

```

The infrastructure is provisioned using Terraform while GitHub Actions enforces automated validation before code changes are accepted.

## Project Structure

```

Habot-Hiring-Project/

├── .github/
│ └── workflows/
│ └── ci.yml
│
├── terraform/
│ ├── provider.tf
│ ├── variables.tf
│ ├── terraform.tfvars
│ ├── main.tf
│ └── outputs.tf
│
├── django/
│ ├── serializers.py
│ └── requirements.txt
│
├── .gitignore
└── README.md

```
## Infrastructure Components

Terraform provisions:

- Google Cloud Storage Bucket
- BigQuery Dataset
- IAM Roles
- Least Privilege Access

Security Features:

- Public Access Prevention
- Uniform Bucket Level Access
- IAM Member Bindings
- Secure Infrastructure as Code

## CI/CD Pipeline

The GitHub Actions workflow automatically executes:

- Terraform Format Check
- Terraform Initialization
- Terraform Validation
- TFLint
- Python Linting (Flake8)
- Secret Scanning using Gitleaks

The pipeline follows a Fail-Closed approach.

If any validation fails, the pipeline immediately stops and prevents insecure or incorrectly formatted code from progressing.

## Data Validation

The Django REST Framework serializer validates:

- Student Name
- Parent Name
- Email Address
- Phone Number
- Learning Difficulty
- LSA Requirement
- Consent Status

Validation Rules include:

- Required Fields
- Email Validation
- Phone Number Regex
- Choice Validation
- Business Rule Validation

## Terraform Commands

```bash
terraform init

terraform fmt

terraform validate

terraform plan

terraform apply
```

## GitHub Actions

The CI/CD pipeline is triggered automatically on:

- Push to main branch
- Pull Requests targeting main

Every commit is automatically validated before acceptance.

## Assumptions

The project brief did not provide:

- Actual GCP Project ID
- BigQuery Table Definitions
- Student JSON Schema
- Production IAM Users

Therefore the following assumptions were made:

- A Google Cloud Project exists.
- BigQuery tables will be created after dataset provisioning.
- Row-Level Security will be configured on BigQuery tables after creation.
- Service Accounts are used instead of personal credentials.

## Future Improvements

- Deploy Django application to Google App Engine
- Configure BigQuery Row-Level Security policies
- Implement automated Terraform deployment
- Add unit testing
- Add Docker containerization
- Add monitoring and alerting

## Conclusion

This project demonstrates Infrastructure as Code, CI/CD automation, secure cloud provisioning, and backend request validation using industry best practices.

The implementation focuses on automation, security, maintainability, and data integrity.