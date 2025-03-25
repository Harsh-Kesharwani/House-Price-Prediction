import numpy as np
import pandas as pd
from typing import List, Dict, Union
import xgboost as xgb
import os
import pickle
class HousePricePredictor:
    def __init__(self, model_path=None):
        """
        Initialize the predictor with a pre-trained model
        
        Args:
            model_path (str): Path to the saved model joblib file
        """
        self.model = None
        self.model_path = model_path
        
        if model_path is None:
            model_directory = "./notebook"
            for filename in os.listdir(model_directory):
                print(f"filename: {filename}")
                if filename.endswith(".pkl"):
                    self.model_path = os.path.join(model_directory, filename)
                    print(f"Found model: {self.model_path}")
                    break

        if self.model_path==None:
            raise FileNotFoundError("No model file found in the specified directory.")


        try:
            with open(self.model_path, 'rb') as f:
                self.model = pickle.load(f)
            
            # Convert XGBoost model to Booster if applicable
            if isinstance(self.model, xgb.XGBRegressor):
                self.model = self.model.get_booster()
                print("Loaded XGBoost model as Booster.")
            else:
                print("Loaded model successfully.")
        except Exception as e:
            raise RuntimeError(f"Error loading model: {e}")
        
    
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