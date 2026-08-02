import streamlit as st
import joblib
import os

current_folder = os.path.dirname(__file__)

model_path = os.path.join(current_folder, "student_model.pkl")

model = joblib.load(model_path)

st.title("Student Performance Prediction")

st.write("Enter Student Details")

hours = st.number_input("Study Hours", min_value=0.0, max_value=24.0)

attendance = st.number_input("Attendance (%)", min_value=0.0, max_value=100.0)

assignments = st.number_input("Assignment Score", min_value=0.0, max_value=100.0)

if st.button("Predict"):

    prediction = model.predict([[hours, attendance, assignments]])

    if prediction[0] == 1:
        st.success("Prediction: PASS")
    else:
        st.error("Prediction: FAIL")