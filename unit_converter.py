import streamlit as st
import numpy as np

# Function to convert length
def convert_length(value, from_unit, to_unit):
    length_units = {
        'meter': 1.0,
        'kilometer': 1000.0,
        'mile': 1609.34,
        'yard': 0.9144,
        'foot': 0.3048
    }
    meters = value * length_units[from_unit]
    return meters / length_units[to_unit]

# Function to convert weights
def convert_weight(value, from_unit, to_unit):
    weight_units = {
    'gram': 1.0,
    'kilogram': 1000.0,
    'pound': 453.592,
    'ounce': 28.3495
    }
    grams = value * weight_units[from_unit]
    return grams / weight_units[to_unit]

# Function to convert temperature
def convert_temp(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'Celsius':
        if from_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif from_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32)* 5/9
        elif to_unit == 'Kelvin':
            return (value - 32)* 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value -273.15
        elif to_unit == 'Fahrenheit':
            return (value -273.15)* 9/5 + 32    
        
st.title("Unit Converter App")
category = st.selectbox("Select a category", ['Length', 'Weight', 'Temperature'])
if category == 'Length':
    units = ['meter', 'kilometer', 'mile', 'yard', 'foot']
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter Value:", value = 0.0)
    result = convert_length(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result: .4f} {to_unit}")

elif category == 'Weight':
    units = ['gram', 'kilogram', 'pound', 'ounce']
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter Value:", value = 0.0)
    result = convert_weight(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result: .4f} {to_unit}")

elif category == 'Temperature':
    units = ['Celsius', 'Fahrenheit', 'Kelvin']
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter Value:", value = 0.0)
    result = convert_temp(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result: .2f} {to_unit}")
