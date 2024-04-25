import streamlit as st
import pydeck as pdk

# Sample backup (latitude, longitude, width, height)
data = [
    {"position": [-74.006, 40.7128], "width": 0.1, "height": 0.05},
    {"position": [-73.935242, 40.73061], "width": 0.05, "height": 0.1},
    {"position": [-73.9662, 40.7989], "width": 0.07, "height": 0.07}
]

# Define Pydeck layer
layer = pdk.Layer(
    "ScatterplotLayer",
    data=data,
    get_position="position",
    get_fill_color=[255, 0, 0],
    get_radius=["width", "height", 0]  # Use width and height to define rectangular shape
)

# Define Pydeck map
deck = pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=pdk.ViewState(
        latitude=40.7128,
        longitude=-74.006,
        zoom=10,
        pitch=50,
    ),
    layers=[layer]
)

# Display Pydeck map using Streamlit
st.pydeck_chart(deck)
