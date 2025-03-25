# 🏠 California House Price Prediction 

## 🌟 Project Overview

### Advanced Machine Learning House Price Prediction System
This project demonstrates a complete end-to-end machine learning workflow for predicting house prices using the California Housing Dataset, featuring a robust, modular architecture with modern web technologies.

![Project Banner](https://via.placeholder.com/1200x300.png?text=California+House+Price+Prediction+ML+Project)

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
|   └──EDA_Training.ipynb
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

## 📡 API Endpoints

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

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📜 License

MIT License

## 🙏 Acknowledgements

- Scikit-learn
- XGBoost
- FastAPI
- Streamlit

---

##House Price Prediction Report
##Approach & Decisions

Data Preparation: We used the California housing dataset and performed exploratory data analysis (EDA) using correlation matrices and distribution plots.

Preprocessing: Missing values were checked, and features were standardized using StandardScaler for better model performance.

Model Selection: Four regression models were tested—Linear Regression, Decision Tree, Random Forest, and XGBoost.

Hyperparameter Tuning: GridSearchCV was applied to Decision Tree, Random Forest, and XGBoost to find the best parameters.

Evaluation Metrics: Models were evaluated using RMSE, MAE, and R² scores.

##Model Performance

Linear Regression: Baseline model with RMSE of 0.7456 and R² of 0.5758.

Decision Tree: Improved performance (RMSE: 0.6454, R²: 0.6822) after tuning.

Random Forest: Performed better with RMSE 0.5444 and R² 0.7738.

XGBoost: Best model with RMSE 0.4689 and R² 0.8322.

##Conclusion

XGBoost outperformed other models and was saved as the final model. This approach effectively handled housing price prediction using regression techniques and hyperparameter tuning.

**Happy House Price Predicting!** 🏘️📈