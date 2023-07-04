import pandas as pd
class SpotifySearch():
    def __init__(self, user, sp):
        self.user = user
        self.sp = sp
    # Get songs from playlist URI and user name
    def _process_api_call(self, pl_data, instance='playlist'):
        track_ids = []
        track_names = []
        tracks = pl_data['tracks']['items']
        for i in range(0,len(tracks)):
            if instance=='tracks':
                track_ids.append(tracks[i]['id'])
                track_names.append(tracks[i]['name'])
            else:
                track_ids.append(tracks[i]['track']['id'])
                track_names.append(tracks[i]['track']['name'])
        all_songs = pd.DataFrame({'id': track_ids, 'names': track_names})
        return all_songs
    def get_songs_from_playlistURL(self, plURL):
        pl = self.sp.user_playlist(self.user, plURL)
        pl=self._process_api_call(pl)
        return pl
    def get_playlist_by_genre(self, genre):
        songs = self.sp.search('genre:{}'.format(genre), limit=50, type='track')
        if len(songs) == 0:
            raise ValueError('Genre did not return any results ... try different genre')
        songs=self._process_api_call(songs,instance='tracks')
        return songs
    # Get song feautures
    def get_song_features(all_songs, sp):
        features_df = pd.DataFrame()
        for i in range(0, len(all_songs)):
            audio_features = sp.audio_features(all_songs.loc[i, 'id'])
            af = pd.DataFrame(audio_features)
            
            features_df = pd.concat([features_df, af])
        features_df.set_index('id', inplace = True)
        features_df.drop(['key', 'type', 'mode', 'uri', 'track_href', 'analysis_url', 'time_signature', 'duration_ms'], axis=1, inplace=True)
        return features_df
    # Print results
    def print_crossval_param_scores(grid_result):
        print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
        means = grid_result.cv_results_['mean_test_score']
        stds = grid_result.cv_results_['std_test_score']
        params = grid_result.cv_results_['params']
        for mean, stdev, param in zip(means, stds, params):
            print("%f (%f) with: %r" % (mean, stdev, param))
