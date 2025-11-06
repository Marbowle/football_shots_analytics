import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

SIDE = 'right'
base_path = "D:/football_shots_analytics/data/calibrations/"
src_path = base_path + f"h_{SIDE}_px_points.json"
dts_path = base_path + f"h_{SIDE}_pitch_points.json"
H_path = base_path + f"H_{SIDE}.json"

def open_json_file(path, key):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    data = np.array(data[key], dtype=np.float32)
    return data


src_points = open_json_file(src_path, 'src_points')
dts_points = open_json_file(dts_path, 'dts_points')

with open(H_path, 'r', encoding='utf-8') as f:
    H = np.array(json.load(f), dtype=np.float32)


def project_points(x, y, H):
    vector = [x, y, 1]
    result = H @ vector
    X = result[0] / result[2]
    Y = result[1] / result[2]

    return X, Y

projected_points = []

for (x, y) in src_points:
    (X, Y) = project_points(x, y, H)
    projected_points.append([X, Y])

projected_points = np.array(projected_points)

errors = []

for i in range(len(src_points)):
    dx = projected_points[i][0] - dts_points[i][0]
    dy = projected_points[i][1] - dts_points[i][1]
    dist = math.sqrt(dx**2 + dy**2)
    errors.append(dist)


mean_error = np.mean(errors)
max_error = np.max(errors)

print(f"Walidacja homografii dla {SIDE}")
print(f"Średni błąd to {mean_error}")
print(f"Maksymalny błąd wynosi {max_error}")

if mean_error < 1.0:
    print("Homografia poprawna ")
else:
    print("Homografia wymaga poprawy")

#Create plot
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_facecolor('green')

plt.plot([0,105,105,0,0], [0,0,68,68,0], color='white')

ax.scatter(dts_points[:, 0], dts_points[:, 1], s=40, marker='o', color='blue', label='dts_points(rzeczywiste)')
ax.scatter(projected_points[:, 0], projected_points[:, 1], s=40, marker='x', color='red', label='projected_points(wyliczone)')

for (x1, y1), (x2, y2) in zip(dts_points, projected_points):
    plt.plot([x1, x2], [y1, y2], color='black', linestyle='dashed', linewidth=1)


plt.legend()
plt.title("Sprawdzenie odległości punktów od rzeczywistego położenia")
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
plt.savefig(f"D:/football_shots_analytics/data/calibrations/{SIDE}_pitch_validation.png", dpi=300)


dict = {
    "side": SIDE,
    "mean_error": mean_error,
    "max_error": max_error,
    "projected_points": projected_points,
}
with open(base_path + f"validation_{SIDE}.json", 'w') as f:
    json.dump(dict, f, indent=2, ensure_ascii=False)