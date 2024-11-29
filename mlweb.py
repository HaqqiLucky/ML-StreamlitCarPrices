import streamlit as st

angka = st.number_input(label="Pick a number",min_value=0)
email = st.text_input(label="Email Address")
tanggal = st.date_input(label="Travelling Date")
jam = st.time_input(label="School Time")
desk = st.text_area(label="Deskripsi", height=68)
file = st.file_uploader("Upload foto", type=["jpg","jpeg"])
color = st.color_picker(label="Choose your fav color")