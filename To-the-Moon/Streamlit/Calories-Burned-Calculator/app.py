import streamlit as st
import pickle
import os
import pandas as pd
import numpy as np

if os.environ.get("IS_STREAMLIT_SHARING"):
 model = pickle.load(open('To-the-Moon/Streamlit/Calories-Burned-Calculator/model.sav', 'rb'))
else:
 model = pickle.load(open('model.sav', 'rb'))

st.write("Calories Burned Calculator App")

gender = st.selectbox("Select Gender", ("Male","Female"))

if (gender=="Male"):
 g = 0
else:
 g = 1
 
age = st.number_input("Enter Age", 1, 100, 1)
height = st.number_input("Enter Height in cm", 1, 200, 1)
weight = st.number_input("Enter Weight in kg", 1, 200, 1)
duration = st.number_input("Enter Workout Duration in minutes", 1, 200, 1)
heart_rate = st.number_input("Enter Average Heart Rate", 1, 200, 1) 
body_temp = st.number_input("Enter Body Temperature in Celsius", 1, 100, 1) 
prediction = model.predict(pd.DataFrame(columns=['Gender','Age','Height','Weight','Duration','Heart_Rate','Body_Temp'],
                                         data = np.array([g,age,height,weight,duration,heart_rate,body_temp]).reshape(1,7)))
 
if st.button("Predict"):
 st.success(f"Calories Burned is {round(prediction[0],2)}")