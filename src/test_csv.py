import pandas as pd

df = pd.read_csv('D:/football_shots_analytics/outputs/detections_bundesliga.csv')

print(df['class'].value_counts())
print("++++++++++++++++++")
print(df['confidence'].describe()) #opisywanie wartości znajdujących sie w csv
print(df['confidence'].min()) #sprawdzenie wartości minimalnych w danym zestawie