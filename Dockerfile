FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Train the model before running the app
RUN python3 -m src.train

# Expose the port
EXPOSE 5000

# Run the Flask application
CMD ["python3", "app/main.py"]
