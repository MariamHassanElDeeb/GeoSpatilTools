import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium
import leafmap.foliumap as leafmap
from folium.plugins import Draw

st.set_page_config(
    page_title="Hello",
    page_icon="smile.png",
)
st.write("# Welcome to My GeoTools Project 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    ## I am Mariam Hassan.
    ### This is my Demo for some GeoSpatialTools Project that I made using GeoPandas and leafmap
"""
)