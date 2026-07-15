# Delhi Weather Forecast - REST API Project

A simple Python script that fetches 7-day weather forecast data for Delhi using a public REST API, cleans it with Pandas, and gives a quick summary.

## What it does
- Calls the Open-Meteo weather API (free, no API key needed)
- Gets max/min temperature and rainfall for the next 7 days
- Converts the JSON response into a table using Pandas
- Calculates average temp, hottest day, and total expected rainfall
- Saves everything to a CSV file

## Tech used
- Python
- Requests (for the API call)
- Pandas (for cleaning and analysis)

## How to run
```bash
pip install requests pandas
python rest_api_project.py
```

## Output
Prints the forecast table and summary in the terminal, and saves the data to `delhi_weather_forecast.csv`.

## API used
[Open-Meteo](https://open-meteo.com/) - free weather API, no signup or key required.
