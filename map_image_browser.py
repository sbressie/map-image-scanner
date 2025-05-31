
import streamlit as st
import geopandas as gpd
import pandas as pd
import leafmap.foliumap as leafmap
from PIL import Image
import io

st.set_page_config(page_title="Map & Image Scanner", layout="wide")

st.title("🗺️ Map & Image Scanner (Carto Light Basemap)")

# File uploaders
col1, col2 = st.columns(2)

with col1:
    point_file = st.file_uploader("📍 Upload point file (.geojson, .csv, .shp)", type=["geojson", "csv", "shp", "zip"])
with col2:
    image_file = st.file_uploader("🖼️ Upload image file", type=["jpg", "jpeg", "png"])

# Initialize map
m = leafmap.Map(locate_control=True, draw_control=False, basemap="CartoDB.Positron")

# Process point file
if point_file:
    file_name = point_file.name
    file_ext = file_name.split(".")[-1].lower()

    try:
        if file_ext == "geojson":
            gdf = gpd.read_file(point_file)
        elif file_ext == "csv":
            df = pd.read_csv(point_file)
            if {"latitude", "longitude"}.issubset(df.columns):
                gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude), crs="EPSG:4326")
            else:
                st.error("CSV must have 'latitude' and 'longitude' columns.")
                gdf = None
        elif file_ext in ["shp", "zip"]:
            gdf = gpd.read_file(point_file)
        else:
            gdf = None
            st.warning("Unsupported format")

        if gdf is not None:
            m.add_gdf(gdf, layer_name="Uploaded Points")
            st.success(f"Loaded {len(gdf)} features.")
    except Exception as e:
        st.error(f"Failed to read file: {e}")

# Show map
with st.container():
    st.subheader("🌍 Map Viewer")
    m.to_streamlit(height=600)

# Show image
if image_file:
    st.subheader("🖼️ Uploaded Image")
    try:
        image = Image.open(image_file)
        st.image(image, caption=image_file.name, use_column_width=True)
    except Exception as e:
        st.error(f"Could not display image: {e}")
