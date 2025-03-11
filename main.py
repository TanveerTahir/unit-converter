import streamlit as st


def convert_unit(value, unit_from, unit_to):
    
    # Define the conversion factors
    conversion = {
        "meters_kilometers": 0.001, # 1 meter = 0.001 kilometer
        "kilometers_meters" : 1000,  # 1 kilometer = 1000 meters
        "grams_kilograms"  : 0.001, # 1 gram = 0.001 kilogram
        "kilograms_grams"   : 1000   # 1 kilogram = 1000 grams
    }

    key = f"{unit_from}_{unit_to}" # Create a key to check if the conversion is possible

    # Check if the conversion is possible
    if key in conversion:
        conversion = conversion[key]
        return value * conversion
    else:
        return "Conversion not supported"


st.title("Unit Converter",)

value = st.number_input("Enter the value to convert", min_value=1.0, step=1.0)

unit_form = st.selectbox("Convert From", ["meters", "kilometers", "grams", "kilograms"])

unit_to = st.selectbox("Convert To", ["meters", "kilometers", "grams", "kilograms"])

if st.button("Convert"):
    result = convert_unit(value, unit_form, unit_to)
    st.write(f"Converted Value : {result}")

