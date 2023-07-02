class UserAuth():
    def __init__(self, cid, secret):
        self.cid = cid
        self.secret = secret

    def auth_spotipy(self, scope, redirect_uri):
        sp = spotipy.Spotifu(auth_manager=SpotifyOAuth(self.cid, self.secret, scope=scope, redirect_uri=redirect_uri))
        return sp
