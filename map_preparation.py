import folium

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

map.add_child(folium.LayerControl())

map.save("Templates//Map1.html")
