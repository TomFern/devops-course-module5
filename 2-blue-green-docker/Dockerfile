# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set environment variables to improve Python output and caching
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port that the Flask app runs on
EXPOSE 4000

# Set the default command to run the Flask app
CMD ["python", "app.py"]

