import streamlit as st
import geopandas as gpd
from streamlit_folium import st_folium
import leafmap.foliumap as leafmap

inputFile1 = st.file_uploader("upload geojson file point",type="geojson")
inputFile2 = st.file_uploader("upload geojson file polygon1",type="geojson")
inputFile3 = st.file_uploader("upload geojson polygon2",type="geojson")
buffer_distance = st.text_input("please enter the buffer distance: ")

if  inputFile1 and inputFile2 and inputFile3 :
    buffer_distance= int(buffer_distance)
    point_Read = gpd.read_file(inputFile1).to_crs("EPSG:3857")
    buffer_point = point_Read['geometry'].buffer(buffer_distance)   
    buffer_gdf= gpd.GeoDataFrame(geometry=buffer_point)
    
    polygon1_Read = gpd.read_file(inputFile2).to_crs("EPSG:3857")
    polygon2_Read = gpd.read_file(inputFile3).to_crs("EPSG:3857")
    intersection = gpd.overlay(polygon1_Read, polygon2_Read, how='intersection')
    m = leafmap.Map(center=[40, -100], zoom=4)
    m.add_gdf(buffer_gdf)
    m.add_gdf(polygon1_Read)
    m.add_gdf(polygon2_Read)   
    m.add_gdf(intersection)
    m.add_gdf(point_Read)

    m.to_streamlit(height=500)