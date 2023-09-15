import pandas as pd
import numpy as np
import json
import googlemaps
from datetime import datetime
import polyline
import folium
from folium import plugins

# Chave da API do Google Maps
google_maps_api_key = ""
gmaps = googlemaps.Client(key=google_maps_api_key)


# Carregue os seus dados a partir de um arquivo CSV
df = pd.read_csv("banco_final.csv")

# Extraindo as coordenadas e nomes das escolas
coordinates = df[["lat", "lon"]].values.tolist()
names = df["nome_escola"].tolist()

# Definindo o número máximo de waypoints por solicitação
max_waypoints_per_request = 25

combined_route = []

# Dividindo os waypoints em várias solicitações
for i in range(0, len(coordinates), max_waypoints_per_request - 1):
    start_index = i
    end_index = min(i + max_waypoints_per_request - 1, len(coordinates) - 1)

    # Calcule as direções para o lote atual de waypoints
    waypoints_batch = coordinates[start_index : end_index + 1]
    directions_result = gmaps.directions(
        origin=waypoints_batch[0],
        destination=waypoints_batch[-1],
        waypoints=waypoints_batch[1:-1],  # Exclua o primeiro e o último pontos
        mode="driving",
        optimize_waypoints=True,
    )

    # Extraia a geometria da rota para o lote atual
    route = directions_result[0]["overview_polyline"]["points"]
    decoded_route = polyline.decode(route)

    # Adicione a rota decodificada à rota combinada
    combined_route.extend(decoded_route)

# Adicione uma coluna 'combined_route_order' ao DataFrame com a ordem da rota combinada
df["combined_route_order"] = np.arange(len(df))

# Ordene o DataFrame de acordo com a rota combinada
df = df.iloc[np.argsort(df["combined_route_order"]), :]

# Inicialize o mapa
m = folium.Map(location=[-22.89533, -43.20957], zoom_start=13)

# Adicione a polyline da rota combinada ao mapa
folium.PolyLine(
    locations=combined_route,
    color="blue",  # Cor da linha da rota
    weight=5,  # Espessura da linha
    opacity=0.7,  # Opacidade da linha
).add_to(m)

# Objeto GeoJSON para a rota combinada
route_geojson = {"type": "LineString", "coordinates": combined_route}

# Adicione a rota combinada ao mapa com cor azul
route_layer = folium.GeoJson(
    route_geojson, name="Rota", style_function=lambda x: {"color": "blue", "weight": 5}
).add_to(m)

# Adicione marcadores para as coordenadas
for i, name in enumerate(names):
    folium.Marker(
        location=coordinates[i],
        popup=name,
        icon=folium.Icon(color="green", icon="info-sign"),
    ).add_to(m)

# Adicione um controle de camadas para alternar a exibição da rota
folium.LayerControl().add_to(m)

# Salve o mapa
m.save("rota_mapa.html")
