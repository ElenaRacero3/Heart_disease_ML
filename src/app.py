import streamlit as st
import pandas as pd
import joblib

modelo = joblib.load("model/cardiopatia_model.pkl")

st.set_page_config(layout="wide")
st.header('Web application with integrated machine learning - heart disease')

male = 1 if st.selectbox('Choose your gender:', ["male", "female"], index=None, key=0) == "male" else 0

age = st.slider('Age: ', 21, 82)

currentSmoker = 1 if st.radio('Do you smoke?:', ["Yes", "No"], index=None, key=1) == "Yes" else 0

cigsPerDay = st.slider('Cigarettes per day:: ', 0, 70, key=2)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    BPMeds = 1 if st.radio('Have you had a previous stroke?:', ["Yes", "No"], index=None, key=5) == "Yes" else 0

with col2:
    prevalentStroke = 1 if st.radio('Have you ever taken any blood pressure medication?:', ["Yes", "No"], index=None, key=6) == "Yes" else 0

with col3:
    prevalentHyp = 1 if st.radio('Do you have hypertension?:', ["Yes", "No"], index=None, key=7) == "Yes" else 0

st.divider()

totChol = st.number_input('Cholesterol level: ', key=9, min_value=112, max_value=697)

diabetes = 1 if st.radio('Do you have diabetes?:', ["Yes", "No"], index=None, key=10) == "Yes" else 0

sysBP = st.number_input('Systolic blood pressure: ', key=11, min_value=83, max_value=295)

diaBP = st.number_input('Diastolic blood pressure: ', key=12, min_value=48, max_value=143)

BMI = st.slider('BMI: ', 15, 57, key=13)

heartRate = st.number_input('Heart frequency: ', key=14, min_value=44, max_value=143)

glucose = st.number_input('Glucose level: ', key=15, min_value=40, max_value=395)

if st.button('Submit'):

    X = pd.DataFrame([[male, age, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes, totChol, sysBP, diaBP, BMI, heartRate, glucose]], 
                    columns=['male', 'age', 'currentSmoker', 'cigsPerDay', 'BPMeds', 'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose'])

    prediction = modelo.predict(X)[0]

    st.write(prediction)
        
    if prediction == 0:
        st.text("According to our analysis, your risk of having coronary heart disease (CHD)\nin the next 10 years seems to be low."
                "\nHowever, maintaining a healthy lifestyle is essential to prevent health problems"
                "\nin the future. Keep it up!")
            
    elif prediction == 1:
        st.text("According to our analysis, it seems that you have a high risk of suffering\nfrom coronary heart disease (CHD) in the next 10 years."
                "\nIt is important that you take care of your health."
                "\nRemember, prevention is the best medicine.")
