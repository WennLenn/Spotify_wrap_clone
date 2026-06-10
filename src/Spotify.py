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

# request top 10 artists
results = sp.current_user_top_artists(limit=10)
for idx, artist in enumerate(results["items"], 1):
    top_art_arr = spotidata["top_art"] 
    top_art_arr.insert(idx, artist["name"])


# save the top 10 to a json file
with open("spotidata.json", "w",) as f:
    spotidata["top_art"] = top_art_arr
    json.dump(spotidata, f, indent=2)
    print(spotidata["top_art"])
    
app.run()