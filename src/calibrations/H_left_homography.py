import numpy as np
import matplotlib.pyplot as plt
import cv2
import json

class NumpyAndTupleEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, tuple):
            return list(obj)
        return super().default(obj)

def load_points(path, key):
    with open(path, 'r') as f:
        data = json.load(f)
    points = data[key]
    return np.array([[float(x), float(y)] for x, y in points])

src_points = load_points('D:/football_shots_analytics/data/calibrations/h_left_px_points.json', 'src_points')
dts_points = load_points('D:/football_shots_analytics/data/calibrations/h_left_pitch_points.json', 'dts_points')

if len(src_points) != len(dts_points):
    raise ValueError

#Homography
H_left = cv2.findHomography(src_points, dts_points)


#save as json file
with open("D:/football_shots_analytics/data/calibrations/H_left.json", "w", encoding="utf-8") as f:
    json.dump(H_left, f, cls=NumpyAndTupleEncoder, indent=2)




