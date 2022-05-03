import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from decouple import config

def create_playlist(data,year):
    SPOTIFY_CLIENT_ID=config("SPOTIFY_CLIENT_ID")
    SPOTIFY_CLIENT_SECRET=config("SPOTIFY_CLIENT_SECRET")
    SPOTIFY_REDIRECT_URL=config("SPOTIFY_REDIRECT_URL")

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                                   client_secret=SPOTIFY_CLIENT_SECRET,
                                                   redirect_uri=SPOTIFY_REDIRECT_URL,
                                               scope="playlist-modify-private",
                                                   show_dialog=True,
                                                   cache_path="token.txt"))

    user_id = sp.current_user()["id"]


    song_names = data

    song_urls = []
    year = year
    for song in song_names:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        # print(result)
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_urls.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")

    playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False)
    print(playlist)
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_urls)