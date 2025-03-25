import joblib
import numpy as np
import pandas as pd
from typing import List, Dict, Union
import xgboost as xgb
import os 

class HousePricePredictor:
    def __init__(self, model_path=None):
        """
        Initialize the predictor with a pre-trained model
        
        Args:
            model_path (str, optional): Path to the saved model joblib file
        """
        # Define potential model paths
        possible_paths = [
            model_path,  # User-provided path
            os.path.join('notebook', 'best_house_price_model.joblib'),  # Relative path
            os.path.join(os.path.dirname(__file__), '..', 'notebook', 'best_house_price_model.joblib'),  # Parent directory path
            'best_house_price_model.joblib',  # Current directory
            os.path.abspath('best_house_price_model.joblib')  # Absolute path
        ]
        
        # Try loading the model from multiple possible locations
        for path in possible_paths:
            if path and os.path.exists(path):
                try:
                    self.model = joblib.load(path)
                    
                    # If it's an XGBoost model, convert to Booster if needed
                    if isinstance(self.model, xgb.XGBRegressor):
                        self.model = self.model.get_booster()
                    
                    print(f"Model successfully loaded from {path}")
                    return
                except Exception as e:
                    print(f"Error loading model from {path}: {e}")
        
        # If no model was found, raise an informative error
        raise FileNotFoundError(
            "Could not find the model file. "
            "Please ensure 'best_house_price_model.joblib' is in one of these locations: "
            "notebook/, current directory, or parent directory."
        )
    
    def predict(self, features: Union[np.ndarray, List[float], Dict[str, float]]) -> float:
        """
        Make prediction using the loaded model
        
        Args:
            features (Union[np.ndarray, List[float], Dict[str, float]]): Input features for prediction
        
        Returns:
            float: Predicted house price
        """
        # Convert input to numpy array if it's a dictionary or list
        if isinstance(features, dict):
            # Ensure features are in the correct order based on California Housing dataset
            feature_order = [
                'MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 
                'Population', 'AveOccup', 'Latitude', 'Longitude'
            ]
            features = [features.get(f, 0) for f in feature_order]
        
        # Convert to numpy array and reshape
        X = np.array(features).reshape(1, -1)
        
        # Make prediction based on model type
        if isinstance(self.model, xgb.Booster):
            # Convert to DMatrix for XGBoost Booster
            dtest = xgb.DMatrix(X)
            prediction = self.model.predict(dtest)
        else:
            # Use standard predict for other model types
            prediction = self.model.predict(X)
        
        return float(prediction[0])