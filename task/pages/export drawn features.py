import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium
import leafmap.foliumap as leafmap
from folium.plugins import Draw

m = folium.Map(location=[39.949610, -75.150282], zoom_start=5)
draw= Draw(export=True, filename='drawndatafile.geojson').add_to(m)
output = st_folium(m, width=700, height=500)