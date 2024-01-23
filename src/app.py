import streamlit as st
import pandas as pd
import joblib

modelo = joblib.load("model/cardiopatia_model.pkl")

st.header('Web application with integrated machine learning - heart disease')

male = st.selectbox ('Choose your gender:', ["male", "female"], index=None, key=0)
male = 1 if male == "male" else 0

age = st.slider('Age: ', 21, 82)

currentSmoker = st.radio('Do you smoke?:', ["Yes", "No"], index=None, key=1)
currentSmoker = 1 if currentSmoker == "Yes" else 0

cigsPerDay = st.slider('Cigarettes per day:: ', 0, 70, key=2)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    BPMeds = st.radio('Have you had a previous stroke?:', ["Yes", "No"], index=None, key=5)
    BPMeds = 1 if BPMeds == "Yes" else 0

with col2:
    prevalentStroke = st.radio('Have you ever taken any blood pressure medication?:', ["Yes", "No"], index=None, key=6)
    prevalentStroke = 1 if prevalentStroke == "Yes" else 0


with col3:
    prevalentHyp = st.radio('Do you have hypertension?:', ["Yes", "No"], index=None, key=7)
    prevalentHyp = 1 if prevalentHyp == "Yes" else 0

st.divider()

totChol = st.number_input('Cholesterol level: ', key=9)

diabetes = st.radio('Do you have diabetes?:', ["Yes", "No"], index=None, key=10)
diabetes = 1 if diabetes == "Yes" else 0

sysBP = st.number_input('Systolic blood pressure: ', key=11)

diaBP = st.number_input('Diastolic blood pressure: ', key=12)

BMI = st.slider('BMI: ', 15, 57, key=13)

heartRate = st.number_input('Heart frequency: ', key=14)

glucose = st.number_input('Glucose level: ', key=15)

if st.button('Submit'):
    
    if glucose < 40 or glucose > 395:
        st.error('Glucose level should be between 40 and 395', icon="🚨")

    elif sysBP < 83 or sysBP > 295:
        st.error('Systolic blood pressure should be between 83 and 295', icon="🚨")

    elif diaBP < 48 or diaBP > 143:
        st.error('Diastolic blood pressure should be between 48 and 143', icon="🚨")
    
    elif heartRate < 44 or heartRate > 143:
        st.error('Heart frequency should be between 44 and 143', icon="🚨")
    
    elif totChol < 112 or totChol > 697:
        st.error('Cholesterol level should be between 112 and 697', icon="🚨")

    else:
        
        X = pd.DataFrame([[male, age, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes, totChol, sysBP, diaBP, BMI, heartRate, glucose]], 
                        columns=['male', 'age', 'currentSmoker', 'cigsPerDay', 'BPMeds', 'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose'])

        prediction = modelo.predict(X)[0]

        st.write(prediction)
        
        if prediction == 0:
            st.text("According to our analysis, your risk of having coronary heart disease (CHD)\n in the next 10 years seems to be low."
                    "\nHowever, maintaining a healthy lifestyle is essential to prevent health problems "
                    "\nin the future. Keep it up!")
            
        elif prediction == 1:
            st.text("According to our analysis, it seems that you have a high risk of suffering\n from coronary heart disease (CHD) in the next 10 years."
                    "\nIt is important that you take care of your health. "
                    "\nRemember, prevention is the best medicine.")
