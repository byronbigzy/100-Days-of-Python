import os
import requests
from dotenv import load_dotenv
from datetime import datetime
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET =os.getenv("SPOTIPY_CLIENT_SECRET")
auth_manager = spotipy.SpotifyOAuth(
    client_id=CLIENT_ID, 
    client_secret=CLIENT_SECRET,
    scope="playlist-modify-private",
    redirect_uri="http://127.0.0.1:8080/callback",
    show_dialog=True,
    cache_path="token.txt",
    username="Bigzy"
    )

sp = spotipy.Spotify(auth_manager=auth_manager)

user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type te date in this format YYYY-MM-DD: ")

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0"
}

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}")
content = response.text
soup = BeautifulSoup(content, "html.parser")
songs = soup.select("li ul li h3")
artists = soup.select("li ul li span")
song_names = [song.getText().strip() for song in songs]
artist_names = [artist.getText().strip() for artist in artists[::10]]
year = date.split("-")[0]
search_queries = [f"track: {song} year:{int(year) - 1}-{year}" for song, artist in zip(song_names, artist_names)]

# song_URIs = [sp.search(q=query, limit=1, type="track") for query in search_queries]
track_URIs = []
for query in search_queries:
    try:
        result = sp.search(q=query, limit=1, type="track")
        uri = result["tracks"]['items'][0]['uri']
        track_URIs.append(uri)
    except IndexError:
        print(f"No match found for {query}")
    except Exception as e:
        print(f"An error occoured for query: '{query}': {e}")

new_playlist = sp.user_playlist_create(
    user=user_id,
    name=f"Hot 100 | {date}",
    public=False,
    collaborative=False,
    description=f"A musical trip back in time, to the Top 100 songs on the Billboard chart on {date}"
)

sp.playlist_add_items(playlist_id=new_playlist["id"], items=track_URIs)