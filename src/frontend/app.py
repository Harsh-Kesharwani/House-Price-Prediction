import os
import streamlit as st
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    # Get API URL from environment variable, with a fallback
    api_url = os.getenv('API_URL', 'http://localhost:8000')
    
    st.set_page_config(
        page_title="California House Price Predictor", 
        page_icon=":house:", 
        layout="wide"
    )
    
    # Custom CSS
    st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Title
    st.title("🏠 California House Price Prediction")
    st.markdown("Predict house prices using machine learning")
    
    # Sidebar for feature inputs
    st.sidebar.header("Input House Features")
    
    # Feature input fields
    features = {}
    feature_names = [
        'MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 
        'Population', 'AveOccup', 'Latitude', 'Longitude'
    ]
    
    feature_descriptions = {
        'MedInc': 'Median Income (in $10,000s)',
        'HouseAge': 'House Age (years)',
        'AveRooms': 'Average Number of Rooms',
        'AveBedrms': 'Average Number of Bedrooms',
        'Population': 'Population near the house',
        'AveOccup': 'Average Occupancy',
        'Latitude': 'Latitude of the house location',
        'Longitude': 'Longitude of the house location'
    }
    
    # Dynamic feature input
    for feature in feature_names:
        features[feature] = st.sidebar.number_input(
            feature_descriptions[feature], 
            value=0.0, 
            step=0.1, 
            format="%.2f"
        )
    
    # Display current API URL for transparency
    st.sidebar.info(f"API URL: {api_url}")
    
    # Prediction button
    if st.sidebar.button("Predict House Price"):
        try:
            # Make API request
            response = requests.post(
                f"{api_url}/predict", 
                json={"features": features}
            )
            
            # Check response
            if response.status_code == 200:
                prediction = response.json()['predicted_price']
                st.success(f"Predicted House Price: ${prediction * 100000:.2f}")
                
                # Additional insights
                st.markdown("### Model Insights")
                st.write("Prediction is based on California Housing Dataset")
                st.write("Price is in $100,000 units")
            else:
                st.error("Prediction failed. Please check your inputs.")
        
        except requests.exceptions.ConnectionError:
            st.error(f"Could not connect to the prediction server at {api_url}. Please ensure the API is running.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    
    # Footer
    st.markdown("---")
    st.markdown("Machine Learning House Price Predictor", unsafe_allow_html=True)

if __name__ == "__main__":
    main()