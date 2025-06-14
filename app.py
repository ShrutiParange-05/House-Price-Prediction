import pandas as pd
import pickle as pk
import streamlit as st
model = pk.load(open('C:\\Users\\Shruti\\OneDrive\\Desktop\\House price prediction\\House_price_prediction.pkl', 'rb'))




st.header('Mumbai House Prices Predictor')
data = pd.read_csv('C:/Users/Shruti/OneDrive/Desktop/House price prediction/Cleaned_data.csv')

Loc =st.selectbox('Choose the location',data['Location'].unique())
sqft = st.number_input('Enter Total Sqft')
beds = st.number_input('Enter number of bedrooms')

if st.button('Predict Price'):
    # Make input a DataFrame with correct column names
    input_df = pd.DataFrame([[Loc, sqft, beds]], columns=['Location', 'Total sqft', 'bedrooms'])
    
    # Prediction
    output = model.predict(input_df)
    price = int(output[0] )

    st.success(f'Estimated Price: ₹ {price:,}')