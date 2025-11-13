import pandas as pd

basic_path = "D:/football_shots_analytics/outputs/"

tracks = pd.read_csv(basic_path+"tracks_players_sort.csv")
classes = pd.read_csv(basic_path+"clean_detections_bundesliga.csv")

tracks_sort = tracks.sort_values(by=['frame', 'x1'])
classes_sort = classes.sort_values(by=['frame', 'x1'])

#limitowanie indeksu w ramch klatki
tracks_sort['row_in_frame'] = tracks_sort.groupby('frame').cumcount()
classes_sort['row_in_frame'] = classes_sort.groupby('frame').cumcount()

common_cols = [c for c in tracks_sort.columns if c in classes_sort.columns and c not in ['frame', 'row_in_frame']]

classes_clean = classes_sort.drop(columns=common_cols)

merged_tracks = pd.merge(tracks_sort, classes_clean, on=['frame', 'row_in_frame'])

merged_tracks.to_csv(basic_path+"merged_tracks_bundesliga.csv", index=False)