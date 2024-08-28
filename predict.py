# src/predict.py

import pandas as pd
import joblib

def load_data(file_path):
    """
    Load new data for prediction from a CSV file.
    
    Parameters:
    file_path (str): Path to the CSV file.
    
    Returns:
    pd.DataFrame: Loaded data.
    """
    return pd.read_csv(file_path)

def load_model(model_path):
    """
    Load the trained model from a file.
    
    Parameters:
    model_path (str): Path to the model file.
    
    Returns:
    RandomForestRegressor: Loaded model.
    """
    return joblib.load(model_path)

def make_predictions(model, df):
    """
    Make predictions using the trained model.
    
    Parameters:
    model (RandomForestRegressor): The trained model.
    df (pd.DataFrame): Data to make predictions on.
    
    Returns:
    pd.Series: Predictions.
    """
    return model.predict(df)

if __name__ == "__main__":
    data = load_data('data/new_data.csv')  # Replace with the path to your new data
    model = load_model('models/saved_model.h5')
    predictions = make_predictions(model, data)
    predictions_df = pd.DataFrame(predictions, columns=['Predictions'])
    predictions_df.to_csv('data/predictions.csv', index=False)
    print("Predictions complete. Results saved to 'data/predictions.csv'.")
