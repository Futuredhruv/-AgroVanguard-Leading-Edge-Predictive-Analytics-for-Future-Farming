# src/train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

def load_data(file_path):
    """
    Load the dataset from a CSV file.
    
    Parameters:
    file_path (str): Path to the CSV file.
    
    Returns:
    pd.DataFrame: Loaded data.
    """
    return pd.read_csv(file_path)

def train_model(df):
    """
    Train a RandomForestRegressor model.
    
    Parameters:
    df (pd.DataFrame): The dataset including features and target.
    
    Returns:
    RandomForestRegressor: Trained model.
    """
    X = df.drop('target', axis=1)  # Features
    y = df['target']               # Target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    return model

if __name__ == "__main__":
    data = load_data('data/engineered_dataset.csv')
    model = train_model(data)
    joblib.dump(model, 'models/saved_model.h5')
    print("Model training complete. Model saved to 'models/saved_model.h5'.")
