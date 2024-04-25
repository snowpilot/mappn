import streamlit as st
import pandas as pd
import pydeck as pdk
import json
from urllib.error import URLError

st.set_page_config(page_title="Mapping Demo", page_icon="❤️")

st.markdown("# Brussels City Real Estate ❤️ Mappn")
st.sidebar.header("Brussels City Real Estate | Mappn")
st.write(
    """This demo shows the real estate data from Brussels."""
)

# 1. adjusted zoom level
# 2. adjusted center of map
# TODO 3: show scores instead of titles
# TODO 4: change layer names


def get_color_for_score(score):
    score = int(score)
    if score < 20:
        color = [255, 0, 0]
    elif score < 80:
        color = [255, 255, 0]
    else:
        color = [0, 255, 0]

    return color


@st.cache_data
def from_data_file(filename):
    url = (
            "http://localhost:8502/mock_data/" % filename
    )
    st.write(pd.read_json(url))
    return pd.read_json(url)


@st.cache_data
def read_json_file(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        # print(f"backup: {data[0]['score']}")
    return data


try:
    ALL_LAYERS = {
        "Real Estate Locations": pdk.Layer(
            "ScatterplotLayer",
            data=read_json_file("mock_data/property_with_colors.json"),
            get_position=["coordinates_longitude", "coordinates_latitude"],
            # get_color=[200, 30, 0, 160],
            get_fill_color="color",
            # get_radius=200,
            get_radius=[200, 100, 0],
            radius_scale=0.2,
        ),
        "Real Estate Scores": pdk.Layer(
            "TextLayer",
            data=read_json_file("mock_data/property_with_colors.json"),
            get_position=["coordinates_longitude", "coordinates_latitude"],
            get_text="percent",
            get_color=[50, 50, 50, 200],
            get_size=15,
            get_alignment_baseline="'bottom'",
        ),
    }
    st.sidebar.markdown("### Map Layers")
    selected_layers = [
        layer
        for layer_name, layer in ALL_LAYERS.items()
        if st.sidebar.checkbox(layer_name, True)
    ]
    if selected_layers:
        st.pydeck_chart(
            pdk.Deck(
                map_style="mapbox://styles/mapbox/light-v9",
                initial_view_state={
                    "latitude": 50.8460,
                    "longitude": 4.3480,
                    "zoom": 14,
                    "pitch": 50,
                },
                layers=selected_layers,
            )
        )
    else:
        st.error("Please choose at least one layer above.")
except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """
        % e.reason
    )
