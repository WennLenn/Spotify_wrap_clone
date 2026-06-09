import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

with open("client.json", "r", encoding="utf-8") as f:
    client = json.load(f)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id= client["ID"],
    client_secret= client["secret"],
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-top-read"
))

results = sp.current_user_top_artists(limit=20)
for idx, artist in enumerate(results["items"], 1):
    print(idx, artist["name"])