from src.train import train_model
import os

def test_model_training():
    train_model()
    assert os.path.exists('src/model.pkl')
