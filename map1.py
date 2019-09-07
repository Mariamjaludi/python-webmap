import folium
map = folium.Map(location=[51.521925,-0.162761], zoom_start=12, tiles="Stamen Terrain")
fg =folium.FeatureGroup(name="My Map")

fg.add_child(folium.Marker(location=[51.5, -.16], popup="Hi, I am a Marker", icon=folium.Icon(color="green")))
map.add_child(fg)
map.save("Map1.html")
