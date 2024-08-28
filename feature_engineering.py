# src/feature_engineering.py

import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """
    Load preprocessed data from a CSV file.
    
    Parameters:
    file_path (str): Path to the CSV file.
    
    Returns:
    pd.DataFrame: Loaded data.
    """
    return pd.read_csv(file_path)

def engineer_features(df):
    """
    Perform feature engineering to create new features or transform existing ones.
    
    Parameters:
    df (pd.DataFrame): The preprocessed dataset.
    
    Returns:
    pd.DataFrame: Data with engineered features.
    """
    # Example feature engineering: Scale numerical features
    scaler = StandardScaler()
    numerical_features = df.select_dtypes(include=['float64', 'int64'])
    scaled_features = scaler.fit_transform(numerical_features)
    scaled_df = pd.DataFrame(scaled_features, columns=numerical_features.columns)
    
    # Concatenate with non-numerical features
    non_numerical_features = df.select_dtypes(exclude=['float64', 'int64'])
    df_engineered = pd.concat([scaled_df, non_numerical_features], axis=1)

    return df_engineered

if __name__ == "__main__":
    data = load_data('data/preprocessed_dataset.csv')
    engineered_data = engineer_features(data)
    engineered_data.to_csv('data/engineered_dataset.csv', index=False)
    print("Feature engineering complete. Engineered data saved to 'data/engineered_dataset.csv'.")

