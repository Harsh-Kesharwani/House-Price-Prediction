from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import logging
import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('app.log')
    ]
)
logger = logging.getLogger(__name__)

# Import the predictor
from src.model.predict import HousePricePredictor

# Create FastAPI app with configurable title from environment
app = FastAPI(
    title=os.getenv('API_TITLE', 'California House Price Prediction API'),
    description=os.getenv('API_DESCRIPTION', 'API for predicting house prices using a pre-trained machine learning model'),
    version=os.getenv('API_VERSION', '1.0.0')
)

# Prediction Request Model
class PredictionRequest(BaseModel):
    features: Dict[str, float]

# Prediction Response Model
class PredictionResponse(BaseModel):
    predicted_price: float

# Initialize predictor
predictor = HousePricePredictor()

@app.post("/predict", response_model=PredictionResponse)
async def predict_house_price(request: PredictionRequest):
    """
    Endpoint to predict house price based on input features
    
    Args:
        request (PredictionRequest): Input features for prediction
    
    Returns:
        PredictionResponse: Predicted house price
    """
    try:
        logger.info(f"Received prediction request with features: {request.features}")
        
        # Perform prediction
        predicted_price = predictor.predict(request.features)
        
        logger.info(f"Predicted price: ${predicted_price:.2f}")
        
        return {"predicted_price": predicted_price}
    
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

# Health check endpoint
@app.get("/health")
async def health_check():
    """
    Simple health check endpoint
    
    Returns:
        dict: Health status
    """
    return {"status": "healthy"}