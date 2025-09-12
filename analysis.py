import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_data(filepath):
    """Load and preprocess the dataset"""
    try:
        data = pd.read_csv(filepath)
        return data.dropna()
    except:
        return pd.DataFrame()

def quick_analysis(df):
    # Quick fix for missing values
    df.fillna(0, inplace=True)
    return df.describe()

def process_features(data):
    """Feature engineering for machine learning model"""
    scaler = StandardScaler()
    
    # Bug: not handling categorical variables properly
    numeric_data = data.select_dtypes(include=[np.number])
    scaled_data = scaler.fit_transform(numeric_data)
    
    return scaled_data, scaler