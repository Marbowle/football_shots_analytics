import pandas as pd
import cv2

#base path to file
base_path = "D:/football_shots_analytics/"

df = pd.read_csv(base_path+"outputs/clean_detections_bundesliga.csv")

print(df.head())

#base vidoe to save csv
cap = cv2.VideoCapture(base_path+"data/clips/match_shorts/bundesliga.mp4")

#proper width of video
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
half_width = width / 2

#additional variables
last_known_ball_x = None
last_side = 'unknown'
sides = []

for frame_id in df['frame'].unique():
    ball_cx = None
    detections = df[df['frame'] == frame_id]

    #
    ball_detections = detections[detections['class'] == 'sports ball']

    if len(ball_detections) > 0:
        x1= float(ball_detections['x1'].iloc[0])
        x2 = float(ball_detections['x2'].iloc[0])
        ball_cx = (x1 + x2) / 2
        last_known_ball_x = ball_cx
    else:
        if last_known_ball_x is not None:
            ball_cx = last_known_ball_x
        else:
            continue

    if ball_cx < half_width:
        side = 'left'
    else:
        side = 'right'
    last_side = side

    df.loc[df['frame'] == frame_id, 'side'] = side

df.to_csv(base_path+"outputs/detections_sides.csv", index=False)