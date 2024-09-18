# Variables
APP_NAME := gcp-compliance-checker
VERSION := 0.1.0
DOCKER_IMAGE := $(APP_NAME):$(VERSION)
PYTHON := python3
PIP := pip3

# Default target
.PHONY: all
all: build

# Build the Docker image
.PHONY: build
build:
	docker build -t $(DOCKER_IMAGE) .

# Run unit tests
.PHONY: test
test:
	$(PYTHON) -m pytest tests/

# Run tests inside Docker
.PHONY: docker-test
docker-test:
	docker run --rm -it $(DOCKER_IMAGE) $(PYTHON) -m pytest tests/

# Clean up Python cache files and Docker images
.PHONY: clean
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache
	docker rmi $(DOCKER_IMAGE) || true

# Rebuild the Docker image (clean build)
.PHONY: rebuild
rebuild: clean build

# Run the application using Docker
.PHONY: run
run:
	docker run --rm -it \
		-e GOOGLE_APPLICATION_CREDENTIALS=/app/credentials.json \
		-v $(PWD)/credentials.json:/app/credentials.json \
		$(DOCKER_IMAGE) --verbose

# Lint the code
.PHONY: lint
lint:
	flake8 src/ tests/

# Install dependencies
.PHONY: deps
deps:
	$(PIP) install -r requirements.txt

# Help message
.PHONY: help
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  build        Build the Docker image."
	@echo "  test         Run unit tests."
	@echo "  docker-test  Run unit tests inside Docker."
	@echo "  run          Run the application using Docker."
	@echo "  clean        Clean up Python cache files and Docker images."
	@echo "  rebuild      Clean and rebuild the Docker image."
	@echo "  lint         Run code linting."
	@echo "  deps         Install dependencies."
	@echo "  help         Show this help message."
