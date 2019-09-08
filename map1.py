import folium
import pandas

# import data from Volcanoes.txt
data = pandas.read_csv("Volcanoes.txt")

# extract latitude and longtitude into separate lists:
lat = list(data['LAT'])
lon = list(data['LON'])

# create map object
map = folium.Map(location=[37.757536,-122.446517], zoom_start=12, tiles="Stamen Terrain")
fg =folium.FeatureGroup(name="My Map")

# use zip to iterate through both lists at the same time.
for lt, ln in zip(lat, lon):
    # assign a point for each volcano
    fg.add_child(folium.Marker(location=[lt, ln], popup="Hi, I am a volcano", icon=folium.Icon(color="green")))

map.add_child(fg)
map.save("Map1.html")
