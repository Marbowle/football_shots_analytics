import pandas as pd
import matplotlib.pyplot as plt

base_path = "D:/football_shots_analytics/"

df = pd.read_csv(base_path + "outputs/detections_pitch_coordinates.csv")

print(df.head())
#chceck cooretnes of calculations
x_m_max = max(df['X_m'])
y_m_max = max(df['Y_m'])
x_m_min = min(df['X_m'])
y_m_min = min(df['Y_m'])
is_na_value = df[['X_m','Y_m']].isna().sum()

print(f"Max value of x: {x_m_max:.2f}")
print(f"Max value of y: {y_m_max:.2f}")
print(f"Min value of x: {x_m_min:.2f}")
print(f"Min value of y: {y_m_min:.2f}")
print(f"Ilosc pustych wartości: {is_na_value}")

#calculate matrics
percent_of_x = ((df['X_m'].between(0,105)).mean()) * 100
percent_of_y = ((df['Y_m'].between(0,68)).mean()) * 100

mean_object_per_frame = (
    df.groupby(['frame', 'class']).size().groupby('class').mean()
)

print(mean_object_per_frame['person'])
print(mean_object_per_frame['sports ball'])

fig, ax = plt.subplots(figsize = (10,6))
ax.plot([0,105,105,0,0], [0,0,68,68,0], color='white')
ax.scatter(df['X_m'], df['Y_m'], c='green', s=10, label='Pozycje')
ax.legend()
plt.title("Walidacja poprawności współrzędnych w metrach")
plt.savefig(base_path + "data/calibrations/validation_pitch.png")
plt.show()

player_df = df[df['track_id'] == 1]
fig, ax = plt.subplots(figsize = (10,6))
ax.plot([0,105,105,0,0], [0,0,68,68,0], color='white')
ax.scatter(player_df['X_m'], player_df['Y_m'], c='red', s=10, label='Pozycje')
ax.legend()
plt.title("Ruch zawondika z track_id = 1")
plt.savefig(base_path + "data/calibrations/player_move.png")
plt.show()
