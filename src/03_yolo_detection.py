from ultralytics import YOLO
import pandas as pd

model = YOLO("yolov8x.pt")

results = model.predict('D:/football_shots_analytics/data/clips/match_shorts/bundesliga.mp4',stream=True ,save=True)
#add info to detection
detections = []
frame_id = 0

for result in results:
    boxes = result.boxes.xyxy
    confs = result.boxes.conf
    classes = result.boxes.cls
    for box, conf, cls in zip(boxes, confs, classes):
        class_name = model.names[int(cls)]
        if class_name in ['person', 'sports ball'] and conf > 0.4:
            x1, y1, x2, y2 = box
            detections.append({
                'frame': frame_id,
                'class': class_name,
                'x1': x1,
                'y1': y1,
                'x2': x2,
                'y2': y2,
                'confidence': conf
            })
    frame_id += 1

#save to csv
df = pd.DataFrame(detections)
df.to_csv("D:/football_shots_analytics/outputs/detections_bundesliga.csv", index=False)
