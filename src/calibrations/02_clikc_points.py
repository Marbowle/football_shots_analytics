import numpy as np
import cv2
import json

points = []

def click_points(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) < 10:
            points.append((x, y))
            print(f"Clicked points: {x}, {y}")
            img_display = img.copy()
            font = cv2.FONT_HERSHEY_SIMPLEX
            label = str(len(points))
            cv2.putText(img_display, label, (x, y), font, 1, (255, 255, 255), 2)
            cv2.circle(img_display, (x, y), 5, (0, 0, 255), 2)
        elif len(points) == 10:
            print("Kliknięto 10 punktów!")
            cv2.destroyAllWindows()

img_path = "/data/calibrations/h_left.png"

img = cv2.imread(img_path)
img_display = img.copy()
cv2.imshow("Process of clicking points", img_display)
cv2.setMouseCallback("Process of clicking points", click_points)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(points)

if len(points) == 10:
    with open("D:/football_shots_analytics/data/calibrations/h_left.json", "w") as f:
        json.dump({"src_pints": points}, f)
    print("Zebrano wystarczającą ilość punktów")
else:
    print("Ta ilość punktów nie wystarczy do poprawnej kalibracji obrazu")