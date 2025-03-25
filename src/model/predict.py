import joblib
import numpy as np
import pandas as pd
from typing import List, Dict, Union
import xgboost as xgb

class HousePricePredictor:
    def __init__(self, model_path='notebook/best_house_price_model.joblib'):
        """
        Initialize the predictor with a pre-trained model
        
        Args:
            model_path (str): Path to the saved model joblib file
        """
        try:
            # Try loading the model with joblib first
            self.model = joblib.load(model_path)
            
            # If it's an XGBoost model, convert to Booster if needed
            if isinstance(self.model, xgb.XGBRegressor):
                self.model = self.model.get_booster()
        except FileNotFoundError:
            raise FileNotFoundError(f"Model not found at {model_path}")
        except Exception as e:
            print(f"Error loading model: {e}")
            raise
    
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