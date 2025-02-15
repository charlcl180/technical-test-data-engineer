import pytest
import requests_mock
import csv
import os
from moovitamix_fastapi.classes_out import TracksOut, UsersOut, ListenHistoryOut
from moovitamix_fastapi.fetch_data import fetch_data, save_to_csv
from datetime import datetime



BASE_URL = "http://127.0.0.1:8000"

def test_fetch_data_tracks():
    """Test que fetch_data() récupère bien les données des tracks et respecte la structure de TracksOut."""
    with requests_mock.Mocker() as m:
        fake_response = [{
            "id": 1, "name": "Song A", "artist": "Artist A",
            "songwriters": "Writer A", "duration": "03:45",
            "genres": "Pop", "album": "Album A",
            "created_at": "2024-02-01T12:00:00", "updated_at": "2024-02-05T15:00:00"
        }]
        m.get(f"{BASE_URL}/tracks", json={"items": fake_response})

        data = fetch_data(f"{BASE_URL}/tracks")
        assert isinstance(data, list)
        assert len(data) == 1

        # Vérification avec le modèle TracksOut
        track = TracksOut(**data[0])
        assert isinstance(track, TracksOut)
        assert track.name == "Song A"
        assert track.artist == "Artist A"

def test_fetch_data_users():
    """Test que fetch_data() récupère bien les données des ussers et respecte la structure de UsersOut."""
    with requests_mock.Mocker() as m:
        fake_response = [{
            "id": 1, "first_name": "Guy", "last_name": "Lafleur", "email": "test@gmail.com",
            "gender": "Male","favorite_genres": "Hip Hop",
            "created_at": "2024-02-01T12:00:00", "updated_at": "2024-02-05T15:00:00"
        }]
        m.get(f"{BASE_URL}/users", json={"items": fake_response})

        data = fetch_data(f"{BASE_URL}/users")
        assert isinstance(data, list)
        assert len(data) == 1

        # Vérification avec le modèle TracksOut
        user = UsersOut(**data[0])
        assert isinstance(user, UsersOut)
        assert user.first_name == "Guy"
        assert user.last_name == "Lafleur"

def test_fetch_data_listen_history():
    """Test que fetch_data() récupère bien les données des listens history et respecte la structure de ListenHistoryOut."""
    with requests_mock.Mocker() as m:
        fake_response = [{
            "user_id": 1, "items": [1, 2, 3, 4, 5],
            "created_at": "2024-02-01T12:00:00", "updated_at": "2024-02-05T15:00:00"
        }]
        m.get(f"{BASE_URL}/listen_history", json={"items": fake_response})

        data = fetch_data(f"{BASE_URL}/listen_history")
        assert isinstance(data, list)
        assert len(data) == 1

        expected_created_at = datetime.strptime("2024-02-01T12:00:00", "%Y-%m-%dT%H:%M:%S")
        expected_updated_at = datetime.strptime("2024-02-05T15:00:00", "%Y-%m-%dT%H:%M:%S")

        # Vérification avec le modèle TracksOut
        listen_history = ListenHistoryOut(**data[0])
        assert isinstance(listen_history, ListenHistoryOut)
        assert listen_history.items == [1, 2, 3, 4, 5]
        assert listen_history.created_at == expected_created_at
        assert listen_history.updated_at == expected_updated_at


def test_fetch_data_empty():
    """Test que fetch_data() gère un cas où l'API renvoie une liste vide."""
    with requests_mock.Mocker() as m:
        m.get(f"{BASE_URL}/tracks", json={"items": []})

        data = fetch_data(f"{BASE_URL}/tracks")
        assert isinstance(data, list)
        assert len(data) == 0  # La liste doit être vide

def test_fetch_data_error():
    """Test que fetch_data() gère correctement une erreur HTTP."""
    with requests_mock.Mocker() as m:
        m.get(f"{BASE_URL}/tracks", status_code=500)  # Simule une erreur 500

        data = fetch_data(f"{BASE_URL}/tracks")
        assert data == []

        
@pytest.fixture
def sample_data():
    """Données factices pour le test"""
    return [
        {"id": 1, "name": "Song A", "artist": "Artist A"},
        {"id": 2, "name": "Song B", "artist": "Artist B"}
    ]

def test_save_to_csv(sample_data, tmp_path):
    """Test que save_to_csv() crée un fichier CSV avec le bon contenu"""
    # Créer un dossier temporaire pour stocker le CSV
    temp_dir = tmp_path / "datas"
    temp_dir.mkdir()

    filename = "test_tracks.csv"
    filepath = temp_dir / filename
    fieldnames = ["id", "name", "artist"]

    # Appeler la fonction avec le dossier temporaire
    save_to_csv(sample_data, filepath, fieldnames)

    # Vérifier si le fichier existe
    assert os.path.exists(filepath)

    # Vérifier le contenu du fichier CSV
    with open(filepath, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    assert len(rows) == len(sample_data)  # Vérifie que toutes les lignes sont présentes
    assert rows[0]["id"] == "1"  # Vérifie la première ligne (CSV stocke tout en string)
    assert rows[0]["name"] == "Song A"
    assert rows[0]["artist"] == "Artist A"