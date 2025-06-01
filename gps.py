import folium
import numpy as np
from sklearn.cluster import DBSCAN
from geopy.distance import great_circle
import json

# Lê os dados do arquivo JSON
with open('detected_people.json', 'r') as f:
    detected_people = json.load(f)

# minha localização atual 
minha_lat = -23.563000
minha_lon = -46.654500

m = folium.Map(location=[minha_lat, minha_lon], zoom_start=17)

coords = np.array([[p["latitude"], p["longitude"]] for p in detected_people])
DIST_MAX_METERS = 20
epsilon = DIST_MAX_METERS / 111_000

db = DBSCAN(eps=epsilon, min_samples=2, metric='haversine')
coords_rad = np.radians(coords)
labels = db.fit_predict(coords_rad)


for group_id in set(labels):
    if group_id == -1:
        continue
    group_points = coords[labels == group_id]
    avg_lat = np.mean(group_points[:, 0])
    avg_lon = np.mean(group_points[:, 1])
    folium.Circle(
        location=[avg_lat, avg_lon],
        radius=DIST_MAX_METERS,
        color='blue',
        fill=True,
        fill_opacity=0.2,
        popup=f'Grupo {group_id}'
    ).add_to(m)

# Marcadores de pessoas
for i, person in enumerate(detected_people):
    folium.Marker(
        [person["latitude"], person["longitude"]],
        popup=f'Pessoa ID: {person["person_id"]} - Grupo: {labels[i]}',
        icon=folium.Icon(color='red', icon='user')
    ).add_to(m)

folium.Marker(
    [minha_lat, minha_lon],
    popup="Minha posição",
    icon=folium.Icon(color='green', icon='star')
).add_to(m)

def nearest_neighbor_path(start, points):
    unvisited = points.copy()
    path = [start]
    while unvisited:
        last = path[-1]
        distances = [great_circle(last, cand).meters for cand in unvisited]
        next_idx = np.argmin(distances)
        path.append(unvisited.pop(next_idx))
    return path

pessoas_coords = [[p["latitude"], p["longitude"]] for p in detected_people]
rota = nearest_neighbor_path([minha_lat, minha_lon], pessoas_coords)

# Plota rota otimizada
folium.PolyLine(
    locations=rota,
    color="purple",
    weight=4,
    opacity=0.7,
    popup="Rota sugerida"
).add_to(m)

m.save('pessoas_detectadas_mapa_grupos.html')
print("Mapa salvo como pessoas_detectadas_mapa_grupos.html")
