import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

# load the pre-trained model and scaler
model = joblib.load('modelss.pkl')
scaler = joblib.load('scalers.save')

def predict_water_quality(ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity):
    # create a dataframe with the user input
    input_data = pd.DataFrame([[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]], 
                              columns=['ph', 'hardness', 'solids', 'chloramines', 'sulfate', 'conductivity', 'organic_carbon', 'trihalomethanes', 'turbidity'])
    # scale the input data
    scaled_data = scaler.transform(input_data)
    # make predictions
    prediction = model.predict(scaled_data)
    return prediction[0]

# create a title for the app
st.title('Water Quality Prediction')
st.header('Enter Spesification Quality Water in this below:')


# create input fields for the user to enter the water quality parameters
ph = st.number_input('Enter the pH of the water')
hardness = st.number_input('Enter the hardness of the water')
solids = st.number_input('Enter the amount of solids in the water')
chloramines = st.number_input('Enter the amount of chloramines in the water')
sulfate = st.number_input('Enter the amount of sulfate in the water')
conductivity = st.number_input('Enter the conductivity of the water')
organic_carbon = st.number_input('Enter the amount of organic carbon in the water')
trihalomethanes = st.number_input('Enter the amount of trihalomethanes in the water')
turbidity = st.number_input('Enter the turbidity of the water')

# when the user clicks the 'Predict' button, make predictions and display the result
if st.button('Predict'):
    prediction = predict_water_quality(ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity)
    if prediction == 0:
        st.write('The water is safe for human consumption.')
    else:
        st.write('The water is not safe for human consumption.')
