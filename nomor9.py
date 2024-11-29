import pickle
import streamlit as st
import pandas as pd
import os
import numpy as np
import altair as alt

# open file csv
df1 = pd.read_csv('CarPrice.csv')

model = pickle.load(open('model_prediksi_harga_mobil.sav', 'rb'))


st.write ('### Hi.. aku adalah navigator web ini')
st.image ('navigator.jpg', width=300,)
st.markdown ('###### Karakter Aether dari Genshin Impact')
st.write (" #### Pilih salah 1 dan kamu akan kena suprise ")
pilihan = st.selectbox(
    'Pilih salah 1 ya',
    ['Silahkan pilih','grapik','dataset','live prediksi']
    )
st.markdown("<hr style='border:3px solid black;'>", unsafe_allow_html=True)

if pilihan == 'grapik':
    st.write("Grafik Highway-mpg")
    chart_highwaympg = pd.DataFrame(df1, columns=['highwaympg'])
    st.line_chart (chart_highwaympg)

    st.write('Grafik curbweight')
    chart_curbweight = pd.DataFrame(df1, columns=['curbweight'])
    st.line_chart(chart_curbweight)

    st.write('Grapik horsepower')
    chart_horsepower = pd.DataFrame(df1, columns=['horsepower'])
    st.line_chart(chart_horsepower)
elif pilihan == 'dataset' :
    st.dataframe(df1)
elif pilihan == 'live prediksi' :
    highwaympg = st.number_input(label='highwaympg')
    curbweight = st.number_input(label='curbweight')
    horsepower = st.number_input(label='horsepower')

    car_prediction = model.predict([[highwaympg,curbweight,horsepower]])

    hargamobil_str = np.array(car_prediction)
    hargamobil_float = float(hargamobil_str[0])
    hargamobil_formatted =(f'Harga Mobil $ {hargamobil_float:,.2f}')
    st.write(hargamobil_formatted)
else : 
    pass

    



# st.title('Prediksi Harga Mobil')

# st.header("Dataset")













# if st.button("Prediksi") :

# else :
#     pass


# st.markdown("#### by lucky")


