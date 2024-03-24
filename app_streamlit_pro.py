import streamlit as st
import numpy as np
import pickle
import random

# Function to load the model
def load_model():
    try:
        model = pickle.load(open("clfmodel.pkl", 'rb'))
        st.write("Model loaded successfully.")
        return model
    except Exception as e:
        st.write("Something went wrong while loading the model.")
        st.write(e)
        return None

# Function to make prediction
@st.cache_data
def make_prediction(_model, features):
    try:
        predicted_label = _model.predict(features)
        return predicted_label
    except Exception as e:
        st.write("Something went wrong while making prediction.")
        st.write(e)
        return None

# Main function to run the app
def main():
    st.title("Custom Grocery App Predictor in Hungary")
    st.write("This app predicts the preferable grocery app based on user characteristics.")

    # Load the model
    clf_model = load_model()

    if clf_model:
        # Sidebar inputs
        st.sidebar.header('User Input Features')
        gender = st.sidebar.radio('Gender', ('Male', 'Female'))
        education = st.sidebar.selectbox('Education Level', ('Under Diploma and Diploma', 'Associate', 'Bachelor', 'Master', 'PhD'))
        age = st.sidebar.slider('Age', 18, 100, 30)
        exp_online = st.sidebar.slider('Years of Online Experience', 0, 50, 5)
        exp_app = st.sidebar.slider('Years of App Experience', 0, 20, 1)

        gender_code = 1 if gender == 'Male' else 2
        education_code = ['Under Diploma and Diploma', 'Associate', 'Bachelor', 'Master', 'PhD'].index(education) + 1

        # Make prediction
        predicted_label = make_prediction(clf_model, np.array([[gender_code, education_code, age, exp_online, exp_app]]))

        if predicted_label is not None:
            class_App_names = ['FoodPanda', 'Wolt', 'Spar', 'Tesco online', 'myLidl']
            predicted_App_class = class_App_names[predicted_label[0] - 1]

            # Generate a random color
            random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))

            # Render the output with only the predicted_App_class colored and bigger font size
            st.write(f"In Hungary, for a {gender}, with education level of {education}, age of {age}, with online experience of {exp_online} years, and shopping experience from online Apps {exp_app} years, It seems that the preferable Grocery App is: ", end="")
            st.markdown(f"<span style='color: {random_color}; font-weight: bold; font-size: 50px'>{predicted_App_class}</span>.", unsafe_allow_html=True)
    else:
        st.write("Failed to load the model.")

if __name__ == '__main__':
    main()
