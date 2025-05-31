import joblib

def predict_salary(years_experience):
    model = joblib.load('src/model.pkl')
    return model.predict([[years_experience]])[0]
