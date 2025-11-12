import streamlit as st
import math
import pickle

with open("model.pkl",'rb') as f:
    model = pickle.load(f)

st.title("🚢 Titanic Survival Prediction")
st.write("Enter passenger details below to predict if they would have **survived** the Titanic tragedy.")


col1, col2,col3 = st.columns(3)
with col1:
    Pclass = st.selectbox("Class of Passenger",("Higher Class","Middle Class","Lower Class"))
with col2:
    Sex = st.selectbox("Gender",("Male","Female"))
with col3:
    Age = st.number_input("Age of passenger", min_value=0, step=1)


col4,col5 = st.columns(2)

with col4:
    SibSp = st.number_input("Siblings/Spouses", min_value=0, step=1)
with col5:
    Parch = st.number_input("Parents/Children", min_value=0, step=1)

col7,col8 = st.columns(2)
with col7:
    Fare = st.number_input("Fare of Journey",  min_value=0.0, step=1.0)
with col8:
    Embarked = st.selectbox("Picking Point",("Cherbourg","Queenstown","Southampton"))

if st.button("🔮 Predict Survival"):
    pclass = 1
    if Pclass=="Lower Class":
        pclass = 3
    elif Pclass=="Middle Class":
        pclass = 2

    gender = 0
    if Sex=="Female":
        gender=1

    age = math.ceil(Age)
    sibsp = math.ceil(SibSp)
    parch = math.ceil(Parch)
    fare = math.ceil(Fare)

    embarked = 0
    if Embarked=="Cherbourg":
        embarked = 1
    elif Embarked=="Queenstown":
        embarked = 2

    result = model.predict([[pclass,gender,age,sibsp,parch,fare,embarked]])
    output_labels = {1: "🌟 The passenger will Survive 🌟",
                     0: "❌ The passenger will NOT Survive ❌"}
    st.markdown(f"## {output_labels[result[0]]}")


