# Use slim Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . .

# Ensure the model is trained before running the app
# Optional: comment this line out if you plan to train and copy model manually
RUN python3 src/train.py

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Run the Flask app
CMD ["python3", "app/main.py"]
