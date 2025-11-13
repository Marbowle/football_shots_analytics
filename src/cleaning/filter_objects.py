import pandas as pd

path = "D:/football_shots_analytics/outputs/detections_pitch_coordinates.csv"

df = pd.read_csv(path)

print(df.head())

to_delete = []
for index, row in df.iterrows():
    if row['X_m'] > 105 and row['Y_m'] > 68:
        to_delete.append(index)

df = df.drop(to_delete)

