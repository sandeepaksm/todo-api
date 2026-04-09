# Use slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies first (layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Remove .env from image (use env vars at runtime)
RUN rm -f .env

# Create non-root user for security
RUN adduser --disabled-password --gecos "" appuser
USER appuser

# Expose port
EXPOSE 8000

# Production command — no --reload
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]

