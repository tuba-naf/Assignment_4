import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Convert height from feet to meters
def feet_to_meters(feet):
    return feet * 0.3048  # 1 foot = 0.3048 meters

# Streamlit App Interface
st.title("BMI (Body Mass Index) Calculator")

# User Input
weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1)

# Height unit selection
height_unit = st.selectbox("Select height unit", ["Meters", "Feet"])

if height_unit == "Meters":
    height = st.number_input("Enter your height (m):", min_value=0.1, step=0.01)
else:  # Height is in feet
    feet = st.number_input("Enter your height (feet):", min_value=1.0, step=0.1)
    height = feet_to_meters(feet)  # Convert feet to meters

# Calculate and Display BMI when button is clicked
if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        st.write(f"Your BMI is: {bmi:.2f}")

        # Display BMI category
        if bmi < 18.5:
            st.write("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.write("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.write("You are overweight.")
        else:
            st.write("You are obese.")
    else:
        st.write("Please enter valid weight and height.")
