import pandas as pd
import streamlit as st

def dataset():
    df_mobil = pd.read_csv("CarPrice.csv")
    return df_mobil

st.sidebar.title("Menu Navigasi")
page = st.sidebar.selectbox(
    "Select Page",
    ['image', 'dataset', 'grapik']
)

if page == 'image':
    st.image("historiml.png", use_container_width=True)
elif page == 'dataset':
    st.write(dataset())
elif page == "grapik":
    df = dataset()         
    st.bar_chart(df['price'])  
else:
    pass
