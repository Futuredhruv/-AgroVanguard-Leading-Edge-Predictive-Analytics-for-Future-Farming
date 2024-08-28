# src/data_preprocessing.py

import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file.
    
    Parameters:
    file_path (str): Path to the CSV file.
    
    Returns:
    pd.DataFrame: Loaded data.
    """
    return pd.read_csv(file_path)

def preprocess_data(df):
    """
    Preprocess the dataset by handling missing values and encoding categorical variables.
    
    Parameters:
    df (pd.DataFrame): The raw dataset.
    
    Returns:
    pd.DataFrame: Preprocessed data.
    """
    # Handle missing values
    df = df.dropna()  # Simple strategy: Drop rows with missing values

    # Encode categorical variables (example: one-hot encoding)
    df = pd.get_dummies(df)

    return df

if __name__ == "__main__":
    data = load_data('data/dataset.csv')
    preprocessed_data = preprocess_data(data)
    preprocessed_data.to_csv('data/preprocessed_dataset.csv', index=False)
    print("Data preprocessing complete. Processed data saved to 'data/preprocessed_dataset.csv'.")
