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
        return "Non-diabetic"
    else:
        return "Diabetic"
    
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
    
# Function to calculate BMI
def calculate_bmi(height, weight):
    height_in_meters = height * 0.0254
    bmi = weight / (height_in_meters ** 2)
    return bmi

# Creating a function to provide advice for non-diabetic people
def non_diabetic_advice(BMI, glucose_level, diastolic_bp):

    advice = "Based on your information, here is some advice for you:"

    if BMI >= 18.5 and BMI <= 24.9:
        advice += "Your BMI is in the healthy range. "
    elif BMI < 18.5:
        advice += "Your BMI is too low. You may want to consider gaining some weight. "
    else:
        advice += "Your BMI is too high. You may want to consider losing some weight. "

    if glucose_level < 100:
        
        advice += "Your glucose level is normal. "
    elif glucose_level >= 100 and glucose_level < 126:
        advice += "Your glucose level is higher than normal. You may be at risk for developing diabetes. Please consult with your healthcare provider. "
    else:
        advice += "Your glucose level is very high. You may have diabetes. Please consult with your healthcare provider. "

    if diastolic_bp < 80:
        advice += "Your diastolic blood pressure is normal. "
    elif diastolic_bp >= 80 and diastolic_bp < 90:
        advice += "Your diastolic blood pressure is higher than normal. You may be at risk for developing hypertension. Please consult with your healthcare provider. "
    else:
        advice += "Your diastolic blood pressure is very high. You may have hypertension. Please consult with your healthcare provider. "
        
    return advice

def main():
    
    # Giving a title
    st.title("Diabetes Prediction Web App")
    
    # Getting the input data from the user 
    
    Pregnancies= st.text_input("Number of Pregnancies")
    Glucose= st.text_input("The Glucose level")
    BloodPressure= st.text_input("Blood pressure value")
    SkinThickness= st.text_input("Skin thickness value")
    Insulin= st.text_input("Insulin value")
    height = st.text_input("Height (inches)")
    weight = st.text_input("Weight (Kg's)")
    DiabetesPedigreeFunction= st.text_input("DiabetesPedigreeFunction value")
    Age= st.text_input("Age of the person")
    BMI = []
    
    # Creating a button to calculate BMI
   if st.button("Calculate BMI"):
        BMI = calculate_bmi(height, weight)
        st.write("Your BMI is:", round(BMI, 2))
    
    # Code for Prediction
    diagnosis= ""
    
    # Creating a button for prediction
    if st.button("Diabetes Test Results"):
        diagnosis= diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
                
        if diagnosis == "Non-diabetic":
            BMI = float(BMI)
            glucose_level = int(Glucose)
            diastolic_bp = int(BloodPressure)

            advice = non_diabetic_advice(BMI, glucose_level, diastolic_bp)

            st.success("You are " + diagnosis + ". " + advice)
        else:
            st.success("You are " + diagnosis + ".")
    
   
    
if __name__ =="__main__":
    main()
    
    
# CODE TO RUN ON THE TERMINAL
# streamlit run "C:\Users\HP\Downloads\Diabetes_ML\diabetes_prediction_web_app.py"
    
    
    
