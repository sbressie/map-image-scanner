# 🗺️ Map & Image Scanner (Streamlit App)

A simple and interactive **Streamlit app** for visualizing **point-based geospatial data** on a **Carto Light basemap**, with support for uploading and previewing a local **image file**.

## 🚀 Features

- 📍 Upload a point dataset (`.geojson`, `.csv`, `.shp`, or zipped shapefile)
- 🗺️ Visualize points on an interactive Leaflet map with the **CartoDB.Positron** basemap
- 🖼️ Upload and preview an image file (`.jpg`, `.png`)
- 🧭 Built using [leafmap](https://leafmap.org), [geopandas](https://geopandas.org), and Streamlit

## 📂 File Support

| File Type | Purpose              | Notes |
|-----------|----------------------|-------|
| `.geojson` | Point or feature data | CRS should be EPSG:4326 |
| `.csv`     | Must include `latitude`, `longitude` columns |
| `.shp/.zip`| Shapefile (single `.shp` or zipped bundle) |
| `.jpg`, `.png` | Image preview         | Displayed in app |

---

## 📦 Requirements

Python dependencies (also included in `requirements.txt`):

```bash
streamlit
geopandas
pandas
leafmap
Pillow
pyogrio
fiona
