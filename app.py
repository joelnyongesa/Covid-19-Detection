import pickle
import numpy as np
import streamlit as st

# Loading the saved XG Boost Model.
loaded_model = pickle.load(open('xgb_model.sav', 'rb'))

# Function to make predictions using the loaded model
def make_prediction(cough, fever, sore_throat, shortness_of_breath, head_ache, age_60_and_above, contact_with_covid_positive_patient, gender, abroad):
    prediction = loaded_model.predict(np.array([[cough, fever, sore_throat, shortness_of_breath, head_ache, age_60_and_above, contact_with_covid_positive_patient, gender, abroad]]))
    return prediction

# Title to introduce the app and its purpose.
st.title("COVID-19 Prediction App")
st.write("This app predicts the likelihood of a person having COVID-19 based on the symptoms and personal details provided.")
# st.write("Please select 0 for 'No' and 1 for 'Yes'")


# Input fields and personal details.
st.write("Please select 0 for 'No' and 1 for 'Yes'")
cough = st.selectbox("Do you have a cough?", [0, 1])
fever = st.selectbox("Do you have a fever?", [0, 1])
sore_throat = st.selectbox("Do you have a sore throat?", [0, 1])
shortness_of_breath = st.selectbox("Do you have shortness of breath?", [0, 1])
head_ache = st.selectbox("Do you have a headache?", [0, 1])
age_60_and_above = st.selectbox("Are you 60 years old or above?", [0, 1])
contact_with_covid_positive_patient = st.selectbox("Have you been in contact with a COVID-19 positive patient?", [0, 1])
st.write("Please select 0 for 'Male' and 1 for 'Female'")
gender = st.selectbox("What is your gender?", [0, 1])
abroad = st.selectbox("Have you traveled abroad recently?", [0, 1])

# Predict button to make the prediction.
if st.button("Predict"):
    prediction = make_prediction(cough, fever, sore_throat, shortness_of_breath, head_ache, age_60_and_above, contact_with_covid_positive_patient, gender, abroad)
    st.write("Your test results: ")
    if prediction[0] == 0:
        st.write("Negative")
    else:
        st.write("Positive")
