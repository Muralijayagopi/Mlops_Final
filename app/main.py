from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

try:
    model = joblib.load("src/model.pkl")
except FileNotFoundError:
    model = None
    print("Model file not found. Please train the model first.")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    if model is None:
        return "Model not loaded. Please train the model first.", 500
    try:
        experience = float(request.form['experience'])
        prediction = model.predict(np.array([[experience]]))[0]
        return render_template("result.html", experience=experience, prediction=round(prediction, 2))
    except ValueError:
        return "Invalid input. Please enter a number.", 400

if __name__ == "__main__":
    app.run(debug=True)
