import streamlit as st
import pandas as pd
import numpy as np

st.write("Here our attempt at using data to create a table")
st.write(pd.DataFrame({
'first column' : [1,2,3,4],
 'second column' : [10,20,30,40]
}))

#highlighting max value

dataframe = pd.DataFrame(
 np.random.randn(10,20),
 columns= ('col %d' % i for i in range (20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

#static table

df2 = pd.DataFrame(
 np.random.randn(10,20),
 columns=('col %d' % i for i in range(20)))
st.table(df2)


#find square using a widget

x = st.slider('y')
st.write(y,'squared is', y * y )

