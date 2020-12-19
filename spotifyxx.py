# # prints all albums of the artist "Birdy"
#
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
#
# birdy_uri = 'spotify:artist:246dkjvS1zLTtiykXe5h60'
# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
#
# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])
# print("Artist:", albums[0]['artists'][0]['name'])
# print("---------------------")
# for album in albums:
#     print(album['name'])
# ---------------------------------------------------------------------------------------------------------
# # prints user's current saved tracks
#
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth

# scope = "user-read-currently-playing"
#
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
# #
# a = sp.current_user_playing_track()
# b = a['item']['album']['artists'][0]['name']
# c = a['item']['name']
# print("Artist:", b)
# print("Playing Song:", c)
#
# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])
# ---------------------------------------------------------------------------------------------------------
# # audio analysis
#
# from __future__ import print_function    # (at top of module)
# from spotipy.oauth2 import SpotifyClientCredentials
# import json
# import spotipy
# import time
# import sys
#
#
# client_credentials_manager = SpotifyClientCredentials()
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#
# if len(sys.argv) > 1:
#     tid = sys.argv[1]
# else:
#     tid = 'spotify:track:4TTV7EcfroSLWzXRY6gLv6'
#
# start = time.time()
# analysis = sp.audio_analysis(tid)
# delta = time.time() - start
# print(json.dumps(analysis, indent=4))
# print("analysis retrieved in %.2f seconds" % (delta,))
# ---------------------------------------------------------------------------------------------------------
# # Shows a user's playlists (need to be authenticated via oauth)
#
# import sys
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
#
# if len(sys.argv) > 1:
#     username = sys.argv[1]
# else:
#     print("Whoops, need a username!")
#     print("usage: python user_playlists.py [username]")
#     sys.exit()
#
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth())
#
# playlists = sp.user_playlists(username)
# spotipy.oauth2.is_token_expired(token_info)
# for playlist in playlists['items']:
#     print(playlist['name'])
# ---------------------------------------------------------------------------------------------------------
# # creates a playlist to the user
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
#
# scope = "playlist-modify-public"
#
# # set open_browser=False to prevent Spotipy from attempting to open the default browser
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, open_browser=False))
# # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(open_browser=False))
#
# playlist_name = "CS464 - Term Project"
# sp.user_playlist_create('hpa6zlnetl6hib5bnp1b5laul', name=playlist_name)
# print("\"", playlist_name, "\" is created")
# ---------------------------------------------------------------------------------------------------------
# # adds tracks to a playlist
# import spotipy
# import base64
# from spotipy.oauth2 import SpotifyOAuth
# #
# scope = 'ugc-image-upload playlist-modify-public playlist-modify-private'
# #
# # # set open_browser=False to prevent Spotipy from attempting to open the default browser
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
# # # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(open_browser=False))
# #
# # playlist_name = "CS464 - Term Project"
# # sp.user_playlist_create('hpa6zlnetl6hib5bnp1b5laul', name=playlist_name)
# # print("\"", playlist_name, "\" is created")
# #
# a = sp.user_playlists('7bodE6U6FML6XzOF8yEFRT', limit=50, offset=0)
# # # print(a)
# # tracks = {'55yvzYuvJYG2RUEnMK78tr', '1bSpwPhAxZwlR2enJJsv7U'}
# # b = sp.tracks(tracks, market='TR')
# # # print(b)
# # # print(b['tracks'][0]['album']['artists'][0]['name'])
# # # print(b['tracks'][0]['name'])
# # # print(b['tracks'][1]['album']['artists'][0]['name'])
# # # print(b['tracks'][1]['name'])
# # # print(a['items'][0]['name'])
# #
# # sp.playlist_add_items(a['items'][0]['id'], tracks, position=None)
# # print("Track: \"", b['tracks'][0]['name'], "\" by \"", b['tracks'][0]['album']['artists'][0]['name'], "\" added to the playlist \"", a['items'][0]['name'], "\"")
# # print("Track: \"", b['tracks'][1]['name'], "\" by \"", b['tracks'][1]['album']['artists'][0]['name'], "\" added to the playlist \"", a['items'][0]['name'], "\"")
# # # aaa = sp.playlist_cover_image(a['items'][0]['id'])
# # with open("bbb.jpeg", "rb") as image_file:
# #     encoded_string = base64.b64encode(image_file.read())
# # print(encoded_string)
# encoded_string = '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'
# sp.playlist_upload_cover_image(playlist_id='spotify:playlist:7bodE6U6FML6XzOF8yEFRT', image_b64=encoded_string)
# # sp.playlist_upload_cover_image(a['items'][0]['id'], encoded_string)
# ---------------------------------------------------------------------------------------------------------
# # gets user's currently playing track
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
#
# scope = "user-read-currently-playing"
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
# a = sp.current_user_playing_track()
# # print(a)
# # print(a['item']['album']['artists'][0]['name'])
# print("Currently playing track is: ", a['item']['name'], "-", a['item']['album']['artists'][0]['name'], "")
# ---------------------------------------------------------------------------------------------------------
# adds a track to the queue
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
#
# scope = "user-modify-playback-state"
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(open_browser=False))
#
# sp.add_to_queue('1nLnpLXvl68RZCSjfkyiaa', device_id=None)

# Creates a playlist of more relevant recommended tracks of a playlist

# install Spotipy first
# !pip install Spotipy

import spotipy
import spotipy.util as util
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import base64
import numpy as np
import warnings
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble.forest import RandomForestRegressor, RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, GridSearchCV
from spotipy.oauth2 import SpotifyOAuth
from sklearn.tree import DecisionTreeClassifier


def playlist_creator(x_train2, y_train2, recorded_indices2, song_info2, spr):
    warnings.filterwarnings('ignore')

    # CELL [9]
    # Random Forests second
    best_score = 0
    skf = StratifiedKFold(n_splits=5, shuffle=True)
    for train_index, test_index in skf.split(x_train2, y_train2):
        # Decision Trees First
        x_train_cv = np.array(x_train2)[train_index, :]
        x_test_cv = np.array(x_train2)[test_index, :]
        y_train_cv = np.array(y_train2)[train_index]
        y_test_cv = np.array(y_train2)[test_index]

        gcv1 = GridSearchCV(RandomForestClassifier(n_estimators=100, n_jobs=-1), n_jobs=-1,param_grid={'max_features': range(3, 6), 'min_samples_leaf': [5, 6, 7],'max_depth': [9, 10, 11, 12, 13]})
        gcv1.fit(x_train_cv, y_train_cv)
        print(gcv1.best_estimator_)
        print(gcv1.best_score_)
        score = gcv1.best_score_
        if score > best_score:
            recorded_train_indexes = train_index
            recorded_test_indexes = test_index
            recorded_best_parameters = gcv1.best_estimator_
    # CELL [10]

    # Make predictions
    X_train_set = np.array(x_train2)[recorded_train_indexes, :]
    X_test_set = np.array(x_train2)[recorded_test_indexes, :]
    y_train_set = np.array(y_train2)[recorded_train_indexes]
    y_test_set = np.array(y_train2)[recorded_test_indexes]
    gcv1.best_estimator_ = recorded_best_parameters
    gcv1.best_estimator_.fit(X_train_set, y_train_set)
    # rec_playlist_df_scaled = StandardScaler().fit_transform(rec_playlist_df)
    # rec_playlist_df_pca = pca1.transform(rec_playlist_df_scaled)
    # X_test_last = csr_matrix(hstack([rec_playlist_df_pca, X_test_names]))
    y_pred_class = gcv1.best_estimator_.predict(X_test_set)
    # print(y_pred_class)
    # CELL [11]
    rec_playlist_ratings = y_pred_class
    # rec_playlist_df = rec_playlist_df.sort_values('ratings', ascending = False)
    # rec_playlist_df = rec_playlist_df.reset_index()
    # Pick the top ranking tracks to add your new playlist 9, 10 will work
    ten_indexes = []
    for k in range(0, len(y_pred_class)):
        if y_pred_class[k] == 10:
            ten_indexes.append(k)
    # recs_to_add = rec_playlist_df[rec_playlist_df['ratings']>=9]['index'].values.tolist()

    recomended_song_indexes = []
    for k in ten_indexes:
        recomended_song_indexes.append(recorded_indices2[0, recorded_test_indexes[k]])
    # for i in nine_indexes:
    #    recomended_song_indexes.append(recorded_indices[0, test_index[i]])
    # print(recomended_song_indexes)

    # Check what is about to happen :)
    # for i in recomended_song_indexes:
    #     print(song_info['id'][i])

    # Create a new playlist for tracks to add - you may also add these tracks to your source playlist and proceed
    # playlist_recs = sp.user_playlist_create(username,
    #                                         name='CS464 - {}'.format(sourcePlaylist['name']))

    # Add tracks to the new playlist
    tracks = {}
    for k in recomended_song_indexes[:3]:
        tracks = {song_info2['id'][k]}
        print(tracks)
        spr.playlist_add_items(playlist_id='7bodE6U6FML6XzOF8yEFRT', items=tracks, position=None)
    return


# CELL [1]
cid = 'a611ab78dcf5445ea1d91bf605134cbd'  # Client ID; copy this from your app created on beta.developer.spotify.com
secret = 'c196412417624657a55c5f71c44fd3b9'  # Client Secret; copy this from your app
username = 'hpa6zlnetl6hib5bnp1b5laul'  # Your Spotify username

# for avaliable scopes see https://developer.spotify.com/web-api/using-scopes/
scope = 'user-library-read playlist-modify-public playlist-read-private user-library-modify'

redirect_uri = 'https://www.google.com.tr/'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

token = util.prompt_for_user_token(username, scope, cid, secret, redirect_uri)

if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)

# CELL [2]
dataset_path = "data.csv"
with open(dataset_path, 'r', encoding="utf8") as token_file:
    lines = csv.reader(token_file)
    dataset = list(lines)
    data = np.array(dataset)
data = data[1:, :]
song_valence = data[:, 17]
song_acousticness = data[:, 0]
song_artists = data[:, 1]
song_danceability = data[:, 2]

song_duration_ms = data[:, 3]
song_energy = data[:, 4]
song_id = data[:, 6]
song_popularity = data[:, 13]

song_instrumentalness = data[:, 7]
song_key = data[:, 8]
song_liveness = data[:, 9]
song_loudness = data[:, 10]

song_mode = data[:, 11]
song_name = data[:, 12]
song_speechiness = data[:, 15]
song_tempo = data[:, 16]
song_year = data[:, 18]

song_info = {'name': [], 'id': [], 'artists': []}
features_dict = {'valence': [], 'year': [], 'popularity': [], 'acousticness': [], 'danceability': [], 'duration_ms': [],
                 'energy': [], 'instrumentalness': [], 'key': [], 'liveness': [], 'loudness': [], 'mode': [],
                 'speechiness': [], 'tempo': []}
for i in range(0, data.shape[0]):
    song_info['name'].append(song_name[i])
    song_info['id'].append(song_id[i])
    song_info['artists'].append(song_artists[i])
    features_dict['valence'].append(song_valence[i])
    features_dict['acousticness'].append(song_acousticness[i])
    features_dict['danceability'].append(song_danceability[i])
    features_dict['duration_ms'].append(song_duration_ms[i])
    features_dict['popularity'].append(song_popularity[i])
    features_dict['energy'].append(song_energy[i])
    features_dict['instrumentalness'].append(song_instrumentalness[i])
    features_dict['key'].append(song_key[i])
    features_dict['liveness'].append(song_liveness[i])
    features_dict['loudness'].append(song_loudness[i])
    features_dict['mode'].append(song_mode[i])
    features_dict['speechiness'].append(song_speechiness[i])
    features_dict['tempo'].append(song_tempo[i])
    features_dict['year'].append(song_year[i])
# playlist_df = pd.DataFrame(features_dict, index=song_info['name'])

# Create a dataframe of your playlist including tracks' names and audio features
sourcePlaylistID = '5TplGaik7PSSBqH6eRRE8E'
sourcePlaylist = sp.user_playlist(username, sourcePlaylistID)
tracks = sourcePlaylist["tracks"]
songs = tracks["items"]

track_ids = []
track_names = []

for i in range(0, len(songs)):
    if songs[i]['track']['id'] != None:  # Removes the local tracks in your playlist if there is any
        track_ids.append(songs[i]['track']['id'])
        track_names.append(songs[i]['track']['name'])

features = []
for i in range(0, len(track_ids)):
    audio_features = sp.audio_features(track_ids[i])
    tr = sp.track(track_ids[i])['popularity']
    year = int(sp.track(track_ids[i])['album']['release_date'][:4])
    for track in audio_features:
        # print(track)
        features.append(track)
    features[i]['popularity'] = tr
    features[i]['year'] = year
playlist_df = pd.DataFrame(features, index=track_names)
features_array = np.zeros((data.shape[0] + 1, 12))

features_array[:data.shape[0], 0] = np.array(features_dict['valence']).T
features_array[:data.shape[0], 1] = np.array(features_dict['acousticness']).T
features_array[:data.shape[0], 2] = np.array(features_dict['danceability']).T
features_array[:data.shape[0], 3] = np.array(features_dict['popularity']).T
features_array[:data.shape[0], 4] = np.array(features_dict['energy']).T
features_array[:data.shape[0], 5] = np.array(features_dict['instrumentalness']).T
features_array[:data.shape[0], 6] = np.array(features_dict['liveness']).T
features_array[:data.shape[0], 7] = np.array(features_dict['loudness']).T
features_array[:data.shape[0], 8] = np.array(features_dict['mode']).T
features_array[:data.shape[0], 9] = np.array(features_dict['speechiness']).T
features_array[:data.shape[0], 10] = np.array(features_dict['tempo']).T
features_array[:data.shape[0], 11] = np.array(features_dict['year']).T

for j in range(0, len(features)):
    indexx = (np.linspace(0, len(features) - 1, num=len(features))).astype(int)
    indexx = np.delete(indexx, j)
    input_ = np.zeros(12)
    input_[0] = (len(features) * playlist_df['valence'][j] + np.sum(playlist_df['valence'][indexx])) / (2 * len(features) - 1)
    input_[1] = (len(features) * playlist_df['acousticness'][j] + np.sum(playlist_df['acousticness'][indexx])) / (2 * len(features) - 1)
    input_[2] = (len(features) * playlist_df['danceability'][j] + np.sum(playlist_df['danceability'][indexx])) / (2 * len(features) - 1)
    input_[3] = (len(features) * playlist_df['popularity'][j] + np.sum(playlist_df['popularity'][indexx])) / (2 * len(features) - 1)
    input_[4] = (len(features) * playlist_df['energy'][j] + np.sum(playlist_df['energy'][indexx])) / (2 * len(features) - 1)
    input_[5] = (len(features) * playlist_df['instrumentalness'][j] + np.sum(playlist_df['instrumentalness'][1:])) / (2 * len(features) - 1)
    input_[6] = (len(features) * playlist_df['liveness'][j] + np.sum(playlist_df['liveness'][indexx])) / (2 * len(features) - 1)
    input_[7] = (len(features) * playlist_df['loudness'][j] + np.sum(playlist_df['loudness'][indexx])) / (2 * len(features) - 1)
    input_[8] = (len(features) * playlist_df['mode'][j] + np.sum(playlist_df['mode'][indexx])) / (2 * len(features) - 1)
    input_[9] = (len(features) * playlist_df['speechiness'][j] + np.sum(playlist_df['speechiness'][indexx])) / (2 * len(features) - 1)
    input_[10] = (len(features) * playlist_df['tempo'][j] + np.sum(playlist_df['tempo'][indexx])) / (2 * len(features) - 1)
    input_[11] = (len(features) * playlist_df['year'][j] + np.sum(playlist_df['year'][indexx])) / (2 * len(features) - 1)

    features_array[data.shape[0], :] = input_

    features_array = features_array.astype('float64')

    model = NearestNeighbors(n_neighbors=5000, algorithm='ball_tree')

    scalar = StandardScaler()
    scalar.fit(features_array)
    features_array = scalar.transform(features_array)
    input_2 = features_array[data.shape[0], :]
    model.fit(features_array[:data.shape[0], :])
    distances, indices = model.kneighbors([input_2])
    recorded_indices = indices

    closest_1000_point = {'valence': [], 'year': [], 'popularity': [], 'mode': [], 'acousticness': [],
                          'danceability': [],
                          'energy': [], 'instrumentalness': [], 'liveness': [], 'loudness': [], 'speechiness': [],
                          'tempo': [], 'ratings': []}

    for k in range(0, 5000):
        closest_1000_point['valence'].append(features_array[indices[0, k], 0])
        closest_1000_point['acousticness'].append(features_array[indices[0, k], 1])
        closest_1000_point['danceability'].append(features_array[indices[0, k], 2])
        closest_1000_point['popularity'].append(features_array[indices[0, k], 3])
        closest_1000_point['energy'].append(features_array[indices[0, k], 4])
        closest_1000_point['instrumentalness'].append(features_array[indices[0, k], 5])
        closest_1000_point['liveness'].append(features_array[indices[0, k], 6])
        closest_1000_point['loudness'].append(features_array[indices[0, k], 7])
        closest_1000_point['mode'].append(features_array[indices[0, k], 8])
        closest_1000_point['speechiness'].append(features_array[indices[0, k], 9])
        closest_1000_point['tempo'].append(features_array[indices[0, k], 10])
        closest_1000_point['year'].append(features_array[indices[0, k], 11])

        rem = k // 500
        closest_1000_point['ratings'].append(10 - rem)
    playlist_dfk = pd.DataFrame(closest_1000_point)
    X_train = playlist_dfk.drop(['ratings'], axis=1)
    y_train = playlist_dfk['ratings']
    playlist_creator(X_train, y_train, recorded_indices, song_info, sp)

# sph = spotipy.Spotify(auth_manager=SpotifyOAuth(scope='ugc-image-upload'))
# CELL [4]
# Change the below info for each playlist manually to get better results
# Give ratings to your tracks with respect to their playlist relevances
# Rate them from 1-10, give higher ratings to those tracks which you think best chracterizes your playlist
# If you order your playlist by relevance while creating it, this step will become easier
# So now, we will deal with a classification task


#     sp.user_playlist_add_tracks(username, playlist_recs['id'], i)
# CELL [12]
# CELL [13]
# CELL [14]
# CELL [15]
# CELL [16]
