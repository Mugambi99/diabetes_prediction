# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle

## Loading the saved model 
loaded_model= pickle.load(open("C:/Users/HP/Downloads/Diabetes_ML/trained_model.sav", "rb"))

# we want to see if our system will predict correctly 
# 1,85,66,29,0,26.6,0.351,31
#input_data= (2,197,70,45,543,30.5,0.158,53)
input_data= (1,85,66,29,0,26.6,0.351,31)
## we need to convert the input_data to a numpy array 

input_data_as_numpy_array= np.asarray(input_data)

## reshaping the instance for one cause we are only doing it for one instance not a whole dataset as we are predicting
input_data_reshape= input_data_as_numpy_array.reshape(1,-1)

prediction= loaded_model.predict(input_data_reshape)
print(prediction)

if prediction[0]== 0:
    print("The person is Non-diabetic")
else:
    print("The person is Diabetic")