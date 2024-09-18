# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the working directory contents into the container at /app
COPY . .

# Expose port if needed (not required for CLI applications)

# Set environment variables for Google Cloud authentication
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/credentials.json"

# Run main.py when the container launches
ENTRYPOINT ["python", "src/main.py"]
