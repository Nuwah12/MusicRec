import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util

# This might be bad practice? 
# Might want to reference functions directly instead of *
from .user_auth import UserAuth 
from .fetch_playlists_songs import Fetcher 
