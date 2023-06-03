# Dockerfile for GitHub Actions CI

# Build phase
FROM python:3.10.10-slim-bullseye AS builder

# Set the working directory
WORKDIR /app

# Install build dependencies
RUN apt-get update && \
    apt-get install -y build-essential

# Copy and install the dependencies
COPY pyproject.toml poetry.lock ./

ENV PIP_DEFAULT_TIMEOUT=1000 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 

RUN pip install poetry

RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi --no-root

# Copy the source code
COPY . .

# Build the server
#RUN poetry build -f wheel && \
#    pip install dist/*.whl

# Runtime phase
FROM python:3.10.10-slim-bullseye

# Set the working directory
WORKDIR /app

# Copy the server binary and its dependencies from the builder image
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /app /app

# Expose the port that the server will listen on
# EXPOSE 50051

# Start the server
CMD cd /app && \
	PYTHONPATH=$PYTHONPATH:. \
	python emotext/httpapi.py --host 0.0.0.0 --port 9003

