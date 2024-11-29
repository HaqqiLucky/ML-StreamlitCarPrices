import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')
st.write('helo,  *World!* :sunglasses:')
st.write(1234)

df = pd.DataFrame(
    np.random.randn(10,2),
    columns=['x','y'])
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)


# df2 = pd.DataFrame(
#     np.random.randn(200,3),
#     columns=['a','b','c']
# )
# c = alt.Chart(df2).mark_circle().encode(
#     x = 'a', y= 'b', size='c', color='c', tooltip=['a','b','c']

# )
# st.write(c)

