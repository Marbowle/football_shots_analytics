import numpy as np
import cv2
import json

SIDE = 'left'

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

src_points = load_points(f'D:/football_shots_analytics/data/calibrations/h_{SIDE}_px_points.json', 'src_points')
dts_points = load_points(f'D:/football_shots_analytics/data/calibrations/h_{SIDE}_pitch_points.json', 'dts_points')

if len(src_points) != len(dts_points):
    raise ValueError

#Homography
H, _ = cv2.findHomography(src_points, dts_points)



#save as json file
with open(f"D:/football_shots_analytics/data/calibrations/H_{SIDE}.json", "w", encoding="utf-8") as f:
    json.dump(H, f, cls=NumpyAndTupleEncoder, indent=2)




