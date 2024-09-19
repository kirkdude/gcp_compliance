# GCP Compliance Checker

## Overview

The **GCP Compliance Checker** is a Python-based framework designed to verify
and enforce compliance rules on Google Cloud SQL instances. It provides a
simple way to define compliance rules, run checks, and remediate issues.

## Features

- **User-Friendly Compliance Rules**: Define rules in JSON format for easy management.
- **Extensible Framework**: Add new compliance checks with minimal code changes.
- **Debugging Tools**: Supports verbose logging, step-through debugging.
- **Cross-Platform Compatibility**: Run on Mac and Linux environments.
- **Docker Support**: Deploy and run the framework in a Docker container.

## Getting Started

### Prerequisites

- **Python 3.7+**
- **Google Cloud SDK** installed and configured and authenticated.

### Authentication

Authenticate with Google Cloud using one of the following methods:

#### Option 1: User Account Authentication

```bash
gcloud auth application-default login
```

This command obtains user credentials that the application uses to call Google Cloud APIs.

#### Option 2: Service Account Authentication

Create a Service Account with the necessary permissions.

Download the Service Account Key (JSON file).

Set the GOOGLE_APPLICATION_CREDENTIALS Environment Variable:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json"
```

### Running the Compliance Checker

#### Directly from Source

```bash
python src/main.py --verbose
```

#### Using Docker

```bash
docker run -v /path/to/credentials.json:/app/credentials.json gcp-compliance-checker --verbose
```

### Setup Development

#### Clone the Repository

```bash
git clone https://github.com/yourusername/gcp_compliance_checker.git
cd gcp_compliance_checker
```

#### Set up the development Environment

```bash
./setup_dev_env.sh
```

#### Running tests

```bash
pytest tests/
```

#### Debugging and Logging

Enable verbose logging to get detailed information about the execution:

```bash
python src/main.py --verbose
```

#### Step-Through Debugging

You can use Python's built-in debugger:

```bash
python -m pdb src/main.py
```

Set breakpoints in the code using:

```bash
import pdb; pdb.set_trace()
```

## Google Cloud Authentication and Permissions

Ensure you have the following permissions:

- Cloud SQL Viewer: To list and get details of Cloud SQL instances.

## Extending the Framework

This framework is designed to be extensible. You can:

- Add Support for Other Resources: Extend the utils.py and checker.py to include checks for other Google Cloud resources.
- Integrate with CI/CD Pipelines: Incorporate the framework into your continuous integration workflows.
- Enhance Error Handling: Improve exception handling for robustness.

## Feedback and Contributions

Feel free to contribute to the project by submitting issues or pull requests on GitHub.
