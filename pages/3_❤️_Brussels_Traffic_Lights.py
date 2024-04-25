import streamlit as st
import pandas as pd
import numpy as np
from random import randrange

colors = [
    [255, 0, 0],  # red
    [255, 255, 0],  # yellow
    [0, 255, 0]  # green
]


index = 0
colorlist = []
while index < 1000:
    index += 1
    color = colors[randrange(3)]
    colorlist.append(color)


df = pd.DataFrame({
    "lat": np.random.randn(1000) / 50 + 50.8445,
    "long": np.random.randn(1000) / 50 + 4.35,
    "size": np.random.randn(1000) * 100,
    "color": colorlist,
})

st.subheader("Brussels Traffic Lights")
# st.write(df)

st.map(df,
       latitude='lat',
       longitude='long',
       size=50,
       color='color',
       zoom=12
       )
