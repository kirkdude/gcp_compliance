# GCP Compliance Checker

## Overview

The **GCP Compliance Checker** is a Python-based framework designed to verify
and enforce compliance rules on Google Cloud SQL instances. It provides a
simple way to define compliance rules, run checks, and remediate issues.

## Features

- **User-Friendly Compliance Rules**: Define rules in JSON format for easy management.
- **Extensible Framework**: Add new compliance checks with minimal code changes.
- **Debugging Tools**: Supports verbose logging, step-through debugging, and dry-run mode.
- **Cross-Platform Compatibility**: Run on Mac and Linux environments.
- **Docker Support**: Deploy and run the framework in a Docker container.

## Getting Started

### Prerequisites

- **Python 3.7+**
- **Google Cloud SDK** installed and configured.
- **Access to a Google Cloud Project** with Cloud SQL instances.
- **Permissions**: Ensure you have at least `Cloud SQL Viewer` permissions.

### Authentication

Authenticate with Google Cloud using one of the following methods:

#### Option 1: User Account Authentication

```bash
gcloud auth application-default login
