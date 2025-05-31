import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_split_data(csv_path='data/salary_data.csv'):
    df = pd.read_csv(csv_path)
    X = df[['YearsExperience']]
    y = df['Salary']
    return train_test_split(X, y, test_size=0.2, random_state=42)
