import streamlit as st
import geopandas as gpd
import folium
import os
import pandas as pd
from streamlit_folium import st_folium
import leafmap.foliumap as leafmap
from folium.plugins import Draw

m = leafmap.Map(center=[40, -100], zoom=4)
inputcsvfile = st.file_uploader("upload csv file contains point")
if inputcsvfile != None:

    filename = inputcsvfile.name
    with open(os.path.join(filename), "w") as f:
        f.write(inputcsvfile.read().decode())
    data = pd.read_csv(filename)

    m.add_points_from_xy(
        data,
        x="longitude",
        y="latitude",
        )
    m.to_streamlit(height=500)