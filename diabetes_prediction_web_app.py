# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 12:19:28 2023

@author: HP
"""

import numpy as np
import pickle
import streamlit as st

## Loading the saved model 
loaded_model= pickle.load(open("trained_model.sav", "rb"))

# Creating a function for prediction
def diabetes_prediction(input_data):

    ## we need to convert the input_data to a numpy array 

    input_data_as_numpy_array= np.asarray(input_data)

    ## reshaping the instance for one cause we are only doing it for one instance not a whole dataset as we are predicting
    input_data_reshape= input_data_as_numpy_array.reshape(1,-1)

    prediction= loaded_model.predict(input_data_reshape)
    print(prediction)

    if prediction[0]== 0:
        return "The person is Non-diabetic"
    else:
        return "The person is Diabetic"
    
st.write("""
    ### Input Data Information
    - Pregnancy: Number of times the patient has been pregnant. This can have an impact on a woman's blood sugar levels and insulin resistance.
    - Glucose: Fasting blood glucose level, a key indicator of diabetes.
    - Blood Pressure: Blood pressure, a common comorbidity associated with diabetes.
    - Skin Thickness: Thickness of skinfold at the triceps, an indicator of body fat composition, which is a risk factor for type 2 diabetes.
    - Insulin: Insulin level, an indicator of insulin sensitivity and metabolic health.
    - BMI: Body mass index, a measure of body fat based on height and weight. High BMI is a common risk factor for type 2 diabetes and other obesity-related health problems.
    - Diabetes Pedigree Function: Genetic risk of diabetes based on family history.
    - Age: Age, a known risk factor for type 2 diabetes.
""")    
    
    
def main():
    
    # Giving a title
    st.title("Diabetes Prediction Web App")
    
    # Getting the input data from the user 
    
    Pregnancies= st.text_input("Number of Pregnancies")
    Glucose= st.text_input("The Glucose level")
    BloodPressure= st.text_input("Blood pressure value")
    SkinThickness= st.text_input("Skin thickness value")
    Insulin= st.text_input("Insulin value")
    BMI= st.text_input("BMI value")
    DiabetesPedigreeFunction= st.text_input("DiabetesPedigreeFunction value")
    Age= st.text_input("Age of the person")
    
    # Code for Prediction
    diagnosis= ""
    
    # Creating a button for prediction
    if st.button("Diabetes Test Results"):
        diagnosis= diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
    
    st.success(diagnosis)    
    
if __name__ =="__main__":
    main()
    
    
# CODE TO RUN ON THE TERMINAL
# streamlit run "C:\Users\HP\Downloads\Diabetes_ML\diabetes_prediction_web_app.py"
    
    
    
