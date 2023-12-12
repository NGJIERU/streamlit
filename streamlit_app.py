import streamlit as st
import pandas as pd
import numpy as np

x = st.slider("Select a value")
st.write(x, "squared is", x * x)

st.button("Reset", type="primary")
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)
