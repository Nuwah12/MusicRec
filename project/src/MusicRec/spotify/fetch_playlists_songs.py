class SpotifySearch():
    def __init__(self):
        pass
    # Get songs from playlist URI and user name
    def get_songs_from_playlistURL(plURL, user, sp):
        track_ids = []
        track_names = []
        tracks = sp.user_playlist(user, plURL)['tracks']['items']

        for i in range(0, len(tracks)):
            track_ids.append(tracks[i]['track']['id'])
            track_names.append(tracks[i]['track']['name'])

        all_songs = pd.DataFrame({'id': track_ids, 'names': track_names})
        song_names = all_songs['names']
        return all_songs
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
