# Use a stable Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.local/bin"

# Copy only dependency files first for better caching
COPY pyproject.toml ./
COPY poetry.lock* ./

# Install dependencies
RUN poetry config virtualenvs.create false && \
    poetry install --only main --no-interaction

# Copy application code
COPY main.py ./

# Create directory for images
RUN mkdir -p ./img && chmod 777 ./img

# Set default environment variables
ENV START_DATE="2015-02-18" \
    END_DATE="2025-12-31" \
    MAX_WORKERS="20"

# Volume for image storage
VOLUME ["./img"]

# Run the application
ENTRYPOINT ["python", "main.py"]