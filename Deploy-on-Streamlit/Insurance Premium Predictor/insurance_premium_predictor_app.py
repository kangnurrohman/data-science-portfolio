import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

nav = st.sidebar.radio("Navigation", ["Home", "Predict", "About"]) 
df = pd.read_csv('insurance.csv')

if nav == "Home":
    st.title("Home")
    st.write("Welcome to the home page!")
    
elif nav == "About":
    st.title("About")
    st.write("Welcome to the about page!")
    st.write("This is a simple web app that predicts the insurance premium of a person based on their")
    st.image('assets/images/insurance.jpeg', width=500)
    
df.replace({'sex':{'male':0,'female':1}}, inplace=True)
df.replace({'smoker':{'yes':0,'no':1}}, inplace=True)
df.replace({'region':{'southwest':0,'southeast':1,'northwest':2,'northeast':3}}, inplace=True)

x = df.drop(columns='charges', axis=1)
y = df['charges']

rfr = RandomForestRegressor()
rfr.fit(x, y)

if nav == "Predict":
    st.title("Predict")
    st.write("Welcome to the prediction page!")
    st.title("Enter details to predict insurance premium")
    
    age = st.number_input("Age", step=1, min_value=0)
    
    sex = st.radio("Sex",("Male","Female"))
    if (sex=="Male"):
        s=0
    if (sex=="Female"):
        s=1
        
    bmi = st.number_input("BMI", min_value=0)
    
    children = st.number_input("Children", step=1, min_value=0)
    
    smoker = st.radio("Smoker",("Yes","No"))
    if (smoker=="Yes"):
        sm=0
    if (smoker=="No"):
        sm=1
        
    region = st.radio("Region",("Southwest","Southeast","Northwest","Northeast"))
    if (region=="Southwest"):
        r=0
    if (region=="Southeast"):
        r=1
    if (region=="Northwest"):
        r=2
    if (region=="Northeast"):
        r=3
    
    if st.button("Predict"):
        output = rfr.predict([[age, s, bmi, children, sm, r]])
        st.success(f"The insurance premium is {output[0]}")
    

