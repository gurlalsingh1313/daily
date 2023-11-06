import streamlit as st

# Define the Streamlit app title and introduction
st.title("Daily Calorie Intake Calculator")
st.write("This calculator estimates your daily calorie intake based on your age, gender, weight, height, and activity level.")

# Input fields for user information
age = st.number_input("Age (years)", 1, 120, 25)
gender = st.radio("Gender", ("Male", "Female"))
weight = st.number_input("Weight (kg)", 1.0, 500.0, 70.0)
height = st.number_input("Height (cm)", 1, 300, 170)
activity_level = st.selectbox(
    "Activity Level",
    ("Sedentary (little or no exercise)", "Lightly active (light exercise/sports 1-3 days/week)", "Moderately active (moderate exercise/sports 3-5 days/week)", "Very active (hard exercise/sports 6-7 days a week)", "Super active (very hard exercise and physical job or 2x training)"))

# Calculate BMR (Basal Metabolic Rate) using Mifflin-St Jeor equation
if gender == "Male":
    bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
else:
    bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

# Calculate TDEE (Total Daily Energy Expenditure) based on activity level
activity_levels = {
    "Sedentary (little or no exercise)": 1.2,
    "Lightly active (light exercise/sports 1-3 days/week)": 1.375,
    "Moderately active (moderate exercise/sports 3-5 days/week)": 1.55,
    "Very active (hard exercise/sports 6-7 days a week)": 1.725,
    "Super active (very hard exercise and physical job or 2x training)": 1.9
}
tdee = bmr * activity_levels[activity_level]

# Display the calculated daily calorie intake
st.write("Your estimated daily calorie intake is approximately:", int(tdee), "calories")
