# Linear Regression ML Pipeline

This project trains a linear regression model to predict salary based on years of experience. It is structured for CI/CD pipelines, testing, and deployment via Flask and Docker.

## Usage
- `python src/train.py`: Train model
- `python app/main.py`: Start Flask app
- POST to `/predict` with `{ \"years_experience\": 5 }`

## Deployment
Supports Docker, GitHub Actions, GCP, and Kubernetes.
