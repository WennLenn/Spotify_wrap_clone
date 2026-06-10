import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
from app import app

# load client data
with open("client.json", "r", encoding="utf-8") as f:
    client = json.load(f)

# set the information
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id= client["ID"],
    client_secret= client["secret"],
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-top-read"
))

# load spotidata json file
with open("spotidata.json", "r") as f:
    spotidata = json.load(f)

limit = 10
# gettop x artists
def top_art():
    results = sp.current_user_top_artists(limit=limit)
    top_art_arr = [artist["name"] for artist in results["items"]]
    spotidata["top_art"] = top_art_arr
    
    with open("spotidata.json", "w", encoding="utf-8") as f:
        json.dump(spotidata, f, indent=2)

# get top x songs
def top_songs():
    results = sp.current_user_top_tracks(limit=limit)
    top_songs_arr = [song["name"] for song in results["items"]]
    spotidata["top_songs"] = top_songs_arr

    with open("spotidata.json", "w", encoding="utf-8") as f:
        json.dump(spotidata, f, indent=2)

top_art()
top_songs()
# run the web app
app.run()