import requests
import csv
import os
from datetime import datetime

# Définir les URLs des endpoints
#test
BASE_URL = "http://127.0.0.1:8000"
ENDPOINTS = {
    "tracks": f"{BASE_URL}/tracks",
    "users": f"{BASE_URL}/users",
    "listen_history": f"{BASE_URL}/listen_history"
}

def fetch_data(endpoint):
    
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        print(f"Erreur {response.status_code} pour {endpoint}")
        return []


def save_to_csv(data, filename, fieldnames):
    filepath = os.path.join("datas", filename)
    
    with open(filepath, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Données enregistrées!")

if __name__ == "__main__":

    # Récupérer les chansons
    tracks_data = fetch_data(ENDPOINTS["tracks"])
    if tracks_data:
        save_to_csv(tracks_data, "tracks.csv", fieldnames=["id", "name", "artist", "songwriters", "duration", "genres", "album", "created_at", "updated_at"])

    # Récupérer les utilisateurs
    users_data = fetch_data(ENDPOINTS["users"])
    if users_data:
        save_to_csv(users_data, "users.csv", fieldnames=["id", "first_name", "last_name", "email", "gender", "favorite_genres", "created_at", "updated_at"])

    # Récupérer l'historique d'écoute
    listen_history_data = fetch_data(ENDPOINTS["listen_history"])
    if listen_history_data:
        save_to_csv(listen_history_data, "listen_history.csv", fieldnames=["user_id", "items", "created_at", "updated_at"])