from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

model_path = "src/model.pkl"

# Load the model with error handling
if not os.path.exists(model_path):
    print(f"⚠️  Model file not found at: {model_path}")
    model = None
else:
    print(f"✅ Loading model from: {model_path}")
    model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    if model is None:
        return render_template("result.html", experience=None, prediction=None, error="Model not loaded. Please train your model first.")
    
    try:
        experience = float(request.form['experience'])
        prediction = model.predict(np.array([[experience]]))[0]
        return render_template("result.html", experience=experience, prediction=round(prediction, 2), error=None)
    except Exception as e:
        return render_template("result.html", experience=None, prediction=None, error=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
