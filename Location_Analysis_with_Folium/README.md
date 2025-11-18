# 🗺️ Lab 6: Launch Site Location Analysis with Folium

## 📌 Objective
To visualize SpaceX Falcon 9 launch sites on an interactive map and analyze their proximity to key geographic features. This lab combines geospatial mapping with distance calculations to explore spatial relationships.

## 🛠️ Tools Used
- `Folium`: For interactive map creation and marker visualization
- `MousePosition`: To inspect coordinates dynamically on the map
- `Haversine formula`: To calculate distances between launch sites and nearby features

## 🔍 Key Activities
- Loaded launch site coordinates from the dataset
- Created a Folium map centered on Florida
- Plotted launch sites using `Marker` and `Circle`
- Added popups with launch site names and metadata
- Marked nearby features:
  - **Coastline**
  - **Highway**
  - **Railway**
  - **City**
- Used the **Haversine formula** to calculate distances from each launch site to these features
- Annotated each site with proximity info (e.g., “Launch site is 3.2 km from nearest railway”)

## 📘 What I Learned
- How to use Folium for interactive geospatial visualization
- How to calculate real-world distances using latitude and longitude
- How to annotate maps with dynamic popups and tooltips
- How spatial context can influence launch logistics and success factors

## 📁 Files in This Folder
- `lab6_location_analysis.ipynb`: Full notebook with Folium map and distance logic
- `README.md`: This documentation

---

**Built by Mukesh — part of my model project series**  
📅 Last updated: September 2025
