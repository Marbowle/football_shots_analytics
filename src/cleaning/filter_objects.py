import pandas as pd
import numpy as np

path = "D:/football_shots_analytics/outputs/detections_pitch_coordinates.csv"

df = pd.read_csv(path)

to_delete = []
for index, row in df.iterrows():
    if row['X_m'] > 105 and row['Y_m'] > 68:
        to_delete.append(index)


df = df.drop(to_delete)

#create list with unique track_id
unique_track_id = df['track_id'].unique().tolist()

referee_list = []

output_list = []

for track_id in unique_track_id:
    data = df[df['track_id'] == track_id].copy()
    mean_x = data['X_m'].mean()
    mean_y= data['Y_m'].mean()

    data['dist'] = np.sqrt((data['X_m'].diff())**2 + (data['Y_m'].diff())**2)
    total_distance = data['dist'].sum()
    output_list.append({
        'track_id': track_id,
        'mean_x': mean_x,
        'mean_y': mean_y,
        'total_distance': total_distance
    })

df = pd.DataFrame(output_list)
df =df.sort_values('total_distance', ascending=False)

max_track_id = df.loc[df['total_distance'].idxmax(), 'track_id']
mean_x_track = df.loc[df['track_id'] == max_track_id, 'mean_x'].iloc[0]


candidate_1 = df.iloc[0]
candidate_2 = df.iloc[1]
candidate_3 = df.iloc[2]

if  45 <= candidate_1['mean_x'] <= 55 :
    referee_list.append(candidate_1['track_id'])
elif 45 <= candidate_2['mean_x'] <= 55 :
    referee_list.append(candidate_2['track_id'])
else:
    referee_list.append(candidate_3['track_id'])



