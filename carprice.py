import pickle
import streamlit as st
import pandas as pd
import os
import numpy as np
import altair as alt

model = pickle.load(open('model_prediksi_harga_mobil.sav', 'rb'))

df1 = pd.read_csv('CarPrice.csv')

menu_options = ["Home", "Highway Chart", "Curbweight Chart", "Horsepower Chart", "Prediction"]

st.sidebar.markdown("<h2 style='text-align: center; color: #FFFFF;'>Menu</h2>", unsafe_allow_html=True)

selected_page = st.sidebar.selectbox("", menu_options)

if selected_page == "Home":
    st.title('Daftar Mobil')
    st.header("Dataset")
    st.dataframe(df1)

elif selected_page == "Highway Chart":
    st.title('Highway Chart')
    chart_highwaympg = pd.DataFrame(df1, columns=["highwaympg"])
    st.line_chart(chart_highwaympg)

elif selected_page == "Curbweight Chart":
    st.title('Curbweight Chart')
    chart_curbweight = pd.DataFrame(df1, columns=["curbweight"])
    st.line_chart(chart_curbweight)

elif selected_page == "Horsepower Chart":
    st.title('Horsepower Chart')
    chart_horsepower = pd.DataFrame(df1, columns=["horsepower"])
    st.line_chart(chart_horsepower)

elif selected_page == "Prediction":
    st.title('Prediksi Harga Mobil')
    highwaympg = st.number_input('Highway-mpg', 0, 10000000)
    curbweight = st.number_input('Curbweight', 0, 10000000)
    horsepower = st.number_input('Horsepower', 0, 10000000)

    if st.button('Prediksi'):
        car_prediction = model.predict([[highwaympg, curbweight, horsepower]])

        actual_vs_predicted = pd.DataFrame({'Actual': df1['actual_column'], 'Predicted': car_prediction})
        st.bar_chart(actual_vs_predicted)

        harga_mobil_str = np.array(car_prediction)
        harga_mobil_float = float(harga_mobil_str[0])

        harga_mobil_formatted = "{:,.2f}".format(harga_mobil_float)
        st.markdown(f'Harga Mobil: $ {harga_mobil_formatted}')

