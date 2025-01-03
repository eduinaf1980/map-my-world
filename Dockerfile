FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

ENV ENVIRONMENT=production

# Initialize Aerich migrations and run the server
CMD ["bash", "-c", "aerich init -t app.main_app.config.TORTOISE_ORM && aerich init-db && uvicorn app.main_app.main:app --host 0.0.0.0 --port 8000"]
