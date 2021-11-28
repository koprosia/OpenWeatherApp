import requests

MY_LAT = 51.507351
MY_LONG = -0.127758
API_KEY = "haba"

weather_params = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "appid": API_KEY,
    "exlude":"current,minutely,daily"
}

response = requests.get(url= "api.openweathermap.org/data/2.5/weather", params=weather_params)
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data["hourly"][:12]
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Brint an umburella!")