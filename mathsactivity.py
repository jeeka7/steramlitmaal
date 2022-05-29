import streamlit as st
import pandas as pd
import numpy as np

st.write("Fun activity of Mathematics")

#find square using a widget

a = st.slider('Enter Value of a',-10,20,0)
b = st.slider('Enter Value of b',-10,20,0)
st.write('(a+b) is', (a+b))
st.write('(a+b)\u00b2 =', (a+b)**2)
st.write('(a-b)\u00b2 =', (a-b)**2)
st.write('(a+b)\u00b3 =', (a+b)**3)
st.write('(a-b)\u00b3 =', (a-b)**3)

if st.button('Click this if you are happy'):
     st.write('Good for you , go make others happy ')
else:
     st.write('Start doing what makes you happy')
