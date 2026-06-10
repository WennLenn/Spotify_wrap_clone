import json
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    json_path = os.path.join(os.path.dirname(__file__), '..', 'spotidata.json')
    json_path = os.path.normpath(json_path)
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    artists = data.get('top_art', [])[:10]
    songs = data.get('top_songs', [])[:10]
    return render_template('index.html', artists=artists, songs=songs)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
