import json
import numpy as np
import pandas as pd

base_path = "D:/football_shots_analytics/"

sides_df = pd.read_csv(base_path + "outputs/detections_sides.csv")

def open_h_calibrations(path):
    with open(path, 'r', encoding='utf-8') as f:
        H = np.array(json.load(f), dtype=np.float32)
    return H

H_left = open_h_calibrations(base_path + "data/calibrations/H_left.json")
H_right = open_h_calibrations(base_path + "data/calibrations/H_right.json")

def projected_points(x,y, H):
    vector = [x,y,1]
    result = H @ vector
    X = result[0]/result[2]
    Y = result[1]/result[2]

    return X,Y

for _, row in sides_df.iterrows():
    cx = (row['x1'] + row['x2'])/2
    cy = (row['y1'] + row['y2'])/2

    if row['side'] == 'left':
        H = H_left
    elif row['side'] == 'right':
        H = H_right
    else:
        continue

    X, Y = projected_points(cx, cy, H)

    sides_df.loc[_,'X_m'] = X
    sides_df.loc[_,'Y_m'] = Y

sides_df.to_csv(base_path + "outputs/detections_pitch_coordinates.csv", index=False)




