import joblib
from sklearn.linear_model import LinearRegression
from src.preprocessing import load_and_split_data
import os

def train_model():
    X_train, X_test, y_train, y_test = load_and_split_data()
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Ensure the model is saved relative to where Flask app expects it
    joblib.dump(model, 'src/model.pkl')
    print("✅ Model trained and saved as 'src/model.pkl'.")

if __name__ == '__main__':
    train_model()
