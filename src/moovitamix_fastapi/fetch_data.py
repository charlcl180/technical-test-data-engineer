import subprocess
import time
import requests
import csv
import os
from datetime import datetime

# Définir les URLs des endpoints
BASE_URL = "http://127.0.0.1:8000"
ENDPOINTS = {
    "tracks": f"{BASE_URL}/tracks",
    "users": f"{BASE_URL}/users",
    "listen_history": f"{BASE_URL}/listen_history"
}

def start_server():
    """Démarre le serveur FastAPI si ce n'est pas déjà fait."""
    try:
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            print("Le serveur FastAPI est déjà en cours d'exécution.")
            return
    except requests.exceptions.ConnectionError:
        print("Démarrage du serveur FastAPI...")
    
    subprocess.Popen(["C:\\Users\\Clayton\\git\\technical-test-data-engineer\\venv\\Scripts\\python.exe", "-m", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"], cwd="src/moovitamix_fastapi")
    
    # Attendre que le serveur démarre
    time.sleep(5)

def fetch_data(endpoint):
    
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json().get("items", [])
    else:
        print(f"Erreur {response.status_code} pour {endpoint}")
        return []


def save_to_csv(data, filename, fieldnames):

    SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))  # = src/moovitamix_fastapi
    DATA_DIR = os.path.join(SCRIPT_DIR, "datas")  # Assure que datas/ est bien dans src/moovitamix_fastapi

    os.makedirs(DATA_DIR, exist_ok=True)

    filepath = os.path.join(DATA_DIR, filename)
   
    with open(filepath, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Données enregistrées!")

if __name__ == "__main__":
    start_server()

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