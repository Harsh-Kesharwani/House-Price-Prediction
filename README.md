# 🏠 California House Price Prediction

## 🌟 Project Overview

### Advanced Machine Learning House Price Prediction System
This project demonstrates a complete end-to-end machine learning workflow for predicting house prices using the California Housing Dataset, featuring a robust, modular architecture with modern web technologies.

![Project Banner](https://via.placeholder.com/1200x300.png?text=California+House+Price+Prediction+ML+Project)

## 🚀 Live Demo
- **Frontend URL**: [House Price Prediction UI](https://house-price-prediction-1-9pla.onrender.com/)
- **Backend API**: [FastAPI Docs](https://house-price-prediction-0cea.onrender.com/docs)

## 🚀 Key Features

- **Machine Learning Model**:
  - Advanced regression techniques
  - XGBoost predictor
  - Comprehensive model evaluation

- **Backend Technology**:
  - FastAPI for high-performance API
  - Robust error handling
  - Comprehensive logging

- **Frontend**:
  - Interactive Streamlit interface
  - Dynamic feature input
  - Real-time predictions

- **Deployment**:
  - Environment-based configuration
  - Easy local setup
  - Containerization ready

## 📦 Project Structure

```
house-price-prediction/
├── notebook/
│   └── best_house_price_model.joblib
│   └── EDA_Training.ipynb
├── src/
│   ├── model/
│   │   └── predict.py
│   ├── api/
│   │   └── main.py
│   └── frontend/
│       └── app.py
├── .env
├── requirements.txt
└── run.sh
```

## 🛠 Prerequisites

- Python 3.11+
- pip
- Virtual Environment (recommended)

## 🔧 Installation & Setup

1. Clone the Repository
```bash
git clone https://github.com/Harsh-Kesharwani/House-Price-Prediction.git
cd house-price-prediction
```

2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Configure Environment
Create a `.env` file in the project root:
```bash
API_HOST=localhost
API_PORT=8000
API_PROTOCOL=http
```

## 🚀 Running the Application

### Method 1: Using Run Script
```bash
chmod +x run.sh
./run.sh
```

### Method 2: Manual Startup
1. Start FastAPI Backend
```bash
uvicorn src.api.main:app --host localhost --port 8000
```

2. Start Streamlit Frontend (in another terminal)
```bash
streamlit run src.frontend.app
```

## 💼 API Endpoints

### Prediction Endpoint
**URL**: `http://localhost:8000/predict`
**Method**: POST

#### Sample Request
```json
{
  "features": {
    "MedInc": 4.5,
    "HouseAge": 35,
    "AveRooms": 4.5,
    "AveBedrms": 1.2,
    "Population": 1500,
    "AveOccup": 3.5,
    "Latitude": 37.5,
    "Longitude": -122.2
  }
}
```

#### Sample Response
```json
{
  "predicted_price": 2.75
}
```
*Note: Price is in $100,000 units*

## 🧪 Feature Details

| Feature      | Description                          | Typical Range      |
|--------------|--------------------------------------|-------------------|
| MedInc       | Median Income (in $10,000s)          | 0.5 - 15          |
| HouseAge     | House Age (years)                    | 1 - 50            |
| AveRooms     | Average Number of Rooms              | 1 - 10            |
| AveBedrms    | Average Number of Bedrooms           | 0.5 - 5           |
| Population   | Population near the house            | 100 - 5000        |
| AveOccup     | Average Occupancy                    | 1 - 5             |
| Latitude     | Geographical Latitude                | 32 - 42           |
| Longitude    | Geographical Longitude               | -124 to -114      |

## 📊 Model Performance

- **Algorithm**: XGBoost Regression
- **RMSE**: 0.68
- **R² Score**: 0.84
- **Mean Absolute Error**: 0.52

## 🔒 Environment Variables

| Variable       | Description                | Default Value    |
|----------------|----------------------------|-----------------|
| API_HOST       | Backend API Host           | localhost       |
| API_PORT       | Backend API Port           | 8000            |
| API_PROTOCOL   | API Connection Protocol    | http            |

## 🏡 House Price Prediction Report

### 📌 Approach & Decisions

**Data Preparation:**
- Used the California Housing dataset
- Conducted Exploratory Data Analysis (EDA)
- Created correlation matrices and distribution plots

**Preprocessing:**
- Checked for missing values
- Standardized features using StandardScaler for improved model performance

**Model Selection:**
- Evaluated multiple regression algorithms:
  - Linear Regression
  - Decision Tree
  - Random Forest
  - XGBoost

**Hyperparameter Tuning:**
- Applied GridSearchCV to optimize:
  - Decision Tree
  - Random Forest
  - XGBoost models

**Evaluation Metrics:**
- Compared models using:
  - Root Mean Square Error (RMSE)
  - Mean Absolute Error (MAE)
  - R² Score

### 📊 Detailed Model Performance Comparison

| Model               | RMSE   | R² Score |
|---------------------|--------|----------|
| Linear Regression   | 0.7456 | 0.5758   |
| Decision Tree       | 0.6454 | 0.6822   |
| Random Forest       | 0.5444 | 0.7738   |
| XGBoost (Best Model)| 0.4689 | 0.8322   |

### ✅ Conclusion

**Key Findings:**
- XGBoost significantly outperformed all other models
- Selected as the final predictor for house price predictions
- Achieved high accuracy through comprehensive regression techniques and rigorous hyperparameter tuning

**Final Model Highlights:**
- Lowest RMSE: 0.4689
- Highest R² Score: 0.8322
- Robust and reliable house price prediction system

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 🐜 License

MIT License

## 🙏 Acknowledgements

- Scikit-learn
- XGBoost
- FastAPI
- Streamlit

**Happy House Price Predicting!** 🏨📈

