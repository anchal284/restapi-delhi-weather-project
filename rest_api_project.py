import requests
import pandas as pd

lat = 28.6139
lon = 77.2090
url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Asia%2FKolkata"

res = requests.get(url)

if res.status_code == 200:
    data = res.json()
    print("data fetched successfully")
else:
    print("error:", res.status_code)
    exit()

daily = data["daily"]

df = pd.DataFrame({
    "date": daily["time"],
    "max_temp_c": daily["temperature_2m_max"],
    "min_temp_c": daily["temperature_2m_min"],
    "rainfall_mm": daily["precipitation_sum"]
})

df["temp_range"] = df["max_temp_c"] - df["min_temp_c"]

print(df)

print("\navg max temp:", round(df["max_temp_c"].mean(), 1))
print("avg min temp:", round(df["min_temp_c"].mean(), 1))
print("hottest day:", df.loc[df["max_temp_c"].idxmax(), "date"])
print("total rainfall:", round(df["rainfall_mm"].sum(), 1), "mm")

df.to_csv("delhi_weather_forecast.csv", index=False)
print("\nsaved to delhi_weather_forecast.csv")