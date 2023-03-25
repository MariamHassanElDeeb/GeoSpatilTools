import streamlit as st
import geopandas as gpd
import leafmap.foliumap as leafmap

point_file = st.file_uploader("Upload Geogson point file", type="geojson")
polygon_file = st.file_uploader("Upload Geogson polygon file ", type="geojson")
if point_file and polygon_file:
    point= gpd.read_file(point_file).to_crs('EPSG:3857')
    polygon= gpd.read_file(polygon_file).to_crs('EPSG:3857')
    joined_data=point.sjoin(polygon)
    m = leafmap.Map()
    m.add_gdf(point, layer_name='Total Points layer')
    m.add_gdf(polygon, layer_name='polygon layer ')
    m.add_gdf(joined_data, layer_name='Point in polygon ')
    m.to_streamlit(height=500)