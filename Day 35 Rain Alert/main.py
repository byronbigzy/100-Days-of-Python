import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv 

API_KEY = os.getenv("API_KEY")
CITY_NAME = os.getenv("CITY_NAME")

params = {
    "q": CITY_NAME,
    "appid": API_KEY,
    "cnt": 4,
    "units": "metric"
}

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast", params=params)
response.raise_for_status()
data = response.json()

will_rain = False

for forecast in data["list"]:
    weather_code = forecast["weather"][0]["id"]
    if int(weather_code) < 700:
        will_rain = True

if will_rain:
    # Send Message
    account_sid = os.getenv("ACCOUNT_SID")
    auth_token = os.getenv("AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Bring an umbrella gang. It finna rain.',
    to='whatsapp:+447969793415'
    )

    print(message.sid)
