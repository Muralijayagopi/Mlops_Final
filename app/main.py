import joblib
import os
from flask import Flask, render_template, request

app = Flask(__name__)

MODEL_PATH = os.path.join('src', 'model.pkl')

try:
    model = joblib.load(MODEL_PATH)
except Exception:
    model = None

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    if model is None:
        return render_template("result.html", prediction="Model not trained yet.")
    
    experience = float(request.form['experience'])
    prediction = model.predict([[experience]])[0]
    return render_template("result.html", experience=experience, prediction=round(prediction, 2))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
