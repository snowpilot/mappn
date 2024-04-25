import streamlit as st
import pandas as pd
import numpy as np
from random import randrange

colors = [
    [255, 0, 0],  # red
    [255, 255, 0],  # yellow
    [0, 255, 0]  # green
]

# 1: changed headline
# 2: removed data
# 3: adjusted zoom level
# 4: centered map

df = pd.DataFrame({
    "lat": np.random.randn(1000) / 50 + 50.8445,
    "long": np.random.randn(1000) / 50 + 4.35,
    "size": np.random.randn(1000) * 100,
    "color": np.random.rand(1000, 4).tolist(),
})

st.subheader("Brussels Random Colors")
# st.write(df)

st.map(df,
       latitude='lat',
       longitude='long',
       size=50,
       color='color',
       zoom=12
       )
