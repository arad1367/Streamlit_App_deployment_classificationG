# Custom Grocery App Predictor in Hungary
This Streamlit app predicts the preferable grocery app in Hungary based on user characteristics.

## Overview
This application is built using Streamlit and a machine learning model trained to predict the preferred grocery app based on user demographics and online shopping experience. 
Users can input their `gender`, `education level`, `age`, `years of online experience`, and `years of app experience` to get a prediction of the most suitable grocery app for them.

## Features
- Predicts the preferable grocery app based on user characteristics.
- Provides an intuitive user interface with input sliders and dropdowns.
- Displays the predicted grocery app in a user-friendly format.

## How to Use
1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Run the Streamlit app by executing streamlit run app_streamlit_pro.py.
3. Input your gender, education level, age, years of online experience, and years of app experience in the sidebar.
4. See real-time prediction that changed based on your input.

## Installation
Clone the repository:
`git clone https://github.com/your_username/custom-grocery-app-predictor.git`

Navigate to the project directory:
`cd custom-grocery-app-predictor`

Install the required dependencies:
`pip install -r requirements.txt`

Run the Streamlit app:
`streamlit run app_streamlit_pro.py` & `python -m streamlit run app_streamlit_pro.py`

## Model
The machine learning model used in this app is a `RandomForestClassifier` trained on historical data of grocery app preferences in Hungary.

## Dataset
The dataset used for training the model is not included in this repository.

## License
This project is licensed under the MIT License.
