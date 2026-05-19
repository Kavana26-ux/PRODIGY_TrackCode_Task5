import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("US_Accidents_March23.csv", nrows=5000)

print(df.head())

df['Start_Time'] = pd.to_datetime(df['Start_Time'])

df['Hour'] = df['Start_Time'].dt.hour

weather = df['Weather_Condition'].value_counts().head(10)

plt.figure(figsize=(10,5))
weather.plot(kind='bar')

plt.title("Accidents by Weather Condition")
plt.xlabel("Weather")
plt.ylabel("Count")
plt.xticks(rotation=45)

plt.show()

plt.figure(figsize=(10,5))

sns.histplot(df['Hour'], bins=24)

plt.title("Accidents by Time of Day")
plt.xlabel("Hour")
plt.ylabel("Accidents")

plt.show()

plt.figure(figsize=(7,5))

sns.countplot(x='Severity', data=df)

plt.title("Accident Severity")
plt.xlabel("Severity")
plt.ylabel("Count")

plt.show()

plt.figure(figsize=(10,6))

plt.scatter(
    df['Start_Lng'],
    df['Start_Lat'],
    s=1,
    alpha=0.5
)

plt.title("Accident Hotspots")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.show()

print("Analysis Completed Successfully")
