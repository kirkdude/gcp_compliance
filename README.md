# GCP Compliance Checker

## Overview

The **GCP Compliance Checker** is a Python-based framework designed to verify
and enforce compliance rules on Google Cloud SQL instances. It provides a
 simple way to define compliance rules, run checks, and remediate issues.

## Features

- **User-Friendly Compliance Rules**: Define rules in JSON format for easy management.
- **Extensible Framework**: Add new compliance checks with minimal code changes.
- **Debugging Tools**: Supports verbose logging and step-through debugging.
- **Cross-Platform Compatibility**: Runs on Mac and Linux environments.
- **Docker Support**: Deploy and run the framework in a Docker container.

## Getting Started

### Prerequisites

- **Python 3.7+**
- **Google Cloud SDK** installed, configured, and authenticated.

### Authentication

Authenticate with Google Cloud using one of the following methods:

#### Option 1: User Account Authentication

```bash
gcloud auth application-default login
```

This command obtains user credentials that the application uses to call Google Cloud APIs.

#### Option 2: Service Account Authentication

1. Create a Service Account with the necessary permissions.
2. Download the Service Account Key (JSON file).
3. Set the `GOOGLE_APPLICATION_CREDENTIALS` Environment Variable:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json"
```

### Running the Compliance Checker

#### Directly from Source

```bash
python src/main.py --verbose
```

#### Using Docker

Build and run the Docker container:

```bash
docker build -t gcp-compliance-checker .
docker run -v /path/to/credentials.json:/app/credentials.json gcp-compliance-checker --verbose
```

### Setup Development Environment

#### Clone the Repository

```bash
git clone https://github.com/kirkdude/gcp_compliance.git
cd gcp_compliance
```

#### Set up the Development Environment

```bash
./setup_dev_env.sh
```

#### Running Tests

Run tests using `pytest`:

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

```python
import pdb; pdb.set_trace()
```

## Docker Usage

The repository contains a `Dockerfile` to build and run the application in a containerized environment.

### Building the Docker Image

```bash
docker build -t gcp-compliance-checker .
```

### Running the Docker Container

```bash
docker run -v /path/to/credentials.json:/app/credentials.json gcp-compliance-checker --verbose
```

Ensure the `GOOGLE_APPLICATION_CREDENTIALS` environment variable points to the correct credentials JSON file.

## Makefile

The repository includes a `Makefile` to simplify common tasks. Available commands include:

- `make install` - Install the dependencies.
- `make test` - Run tests.
- `make lint` - Run linting checks.

To use the `Makefile`, run commands like:

```bash
make install
make test
```

## Google Cloud Authentication and Permissions

Ensure you have the following permissions:

- **Cloud SQL Viewer**: To list and get details of Cloud SQL instances.

## Extending the Framework

This framework is designed to be extensible. You can:

- Add Support for Other Resources: Add your own GCP rules to the compliance_rules directory
- Integrate with CI/CD Pipelines: Incorporate the framework into your continuous integration workflows.
- Enhance Error Handling: Improve exception handling for robustness.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Feedback and Contributions

Feel free to contribute to the project by submitting issues or pull requests on GitHub.
