# Use Python 3.10 slim as base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Train the model (after dependencies are available)
RUN python3 src/train.py

# Expose Flask port
EXPOSE 5000

# Run the app
CMD ["python3", "app/main.py"]
