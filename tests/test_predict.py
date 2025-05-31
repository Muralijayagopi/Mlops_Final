from src.predict import predict_salary

def test_prediction_range():
    salary = predict_salary(5)
    assert salary > 0
