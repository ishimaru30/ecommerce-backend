# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 to match Cloud Run's default port
EXPOSE 8080

# Set environment variable for Flask to listen on the right port
ENV PORT 8080

# Command to run the Flask app
CMD ["python", "main.py"]
