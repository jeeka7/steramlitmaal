import streamlit as st
import pandas as pd
import numpy as np

st.write("Here our attempt at using data to create a table")

#find square using a widget

a = st.slider('Enter Value of a',-10,20,0)
b = st.slider('Enter Value of b',-10,20,0)
st.write('(a+b) square is', (a+b)**2)

