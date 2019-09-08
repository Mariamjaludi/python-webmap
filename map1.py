import folium
import pandas
import json

# import data from Volcanoes.txt
data = pandas.read_csv("Volcanoes.txt")

# extract attributes into separate lists:
lat = list(data['LAT'])
lon = list(data['LON'])
elevation = list(data["ELEV"])
name = list(data["NAME"])
# create map object
map = folium.Map(location=[37.757536,-122.446517], zoom_start=6, tiles="Stamen Terrain")
fg =folium.FeatureGroup(name="My Map")

# html for each point:
html = """<h4>Volcano Information:</h4>
<strong><a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a></strong><br>
Elevation: %s m
"""

# function to assign a color to an elevation range
def color_assign(elev):
    if elev < 1000:
        return "green"
    elif 1000 <= elev < 3000:
        return "orange"
    else:
        return "red"

# use zip to iterate through multiple lists at the same time.
for lt, ln, elev, name in zip(lat, lon, elevation, name):
    # assign a point for each volcano
    iframe = folium.IFrame(html=html % (name, name, elev), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=folium.Popup(iframe), fill_color=color_assign(elev), color = 'grey', fill = True, fill_opacity=0.7))

# add json data
fg.add_child(folium.GeoJson(data=json.load(open('world.json', 'r', encoding='utf-8-sig')),
style_function=lambda x: {'fillColor':'yellow'}))

map.add_child(fg)
map.save("Map1.html")
