import pandas as pd
from filter_objects import referee_list
import numpy as np


path = "D:/football_shots_analytics/outputs/"
df = pd.read_csv(path+"detections_pitch_coordinates.csv")

conditions = [
    (df['class'] == 'sports ball'),
    (df['track_id'].isin(referee_list))
]

values = ['ball', 'referee']

df['role'] = np.select(conditions, values, default='player')

print(df['role'].value_counts())