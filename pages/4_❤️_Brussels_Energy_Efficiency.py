import streamlit as st
import pandas as pd
import numpy as np
from random import randrange

colors = [
    "#C30F11",  # red
    "#E86800",  # dark orange
    "#FCAC13",  # light orange
    "#F2D705",  # yellow
    "#C2C400",  # lime
    "#509F34",  # light green
    "#0C6D23"  # dark green
]

# 1: changed color scale

index = 0
colorlist = []
while index < 1000:
    index += 1
    color = colors[randrange(7)]
    colorlist.append(color)


df = pd.DataFrame({
    "lat": np.random.randn(1000) / 50 + 50.8445,
    "long": np.random.randn(1000) / 50 + 4.3450,
    "size": np.random.randn(1000) * 100,
    "color": colorlist,
})

st.subheader("Brussels Energy Efficiency")
# st.write(df)

st.map(df,
       latitude='lat',
       longitude='long',
       size=50,
       color='color',
       zoom=12
       )
