# Use Python 3.10 slim as base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy everything from the current context to the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Train the model inside the container (ensure salary_data.csv is present)
RUN python3 src/train.py

# Expose the port Flask will run on
EXPOSE 5000

# Start the Flask app
CMD ["python3", "app/main.py"]
