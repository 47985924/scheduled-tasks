import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import pandas as pd


account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

api_key = os.environ.get("OWM_API_KEY")
lat = "48.941132"
lon = "-57.971130"

parameters = {
    "appid": api_key,
    "lat": lat,
    "lon": lon,
    "cnt":4,
}

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
print(response.status_code)
print(data)

will_rain = False
for id in data["list"]:
    id_number = id["weather"][0]["id"]
    print(id_number)
    if int(id_number) < 700:
        will_rain= True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body ="Bring an Umbrella",
        from_='whatsapp:+14155238886',
        to='whatsapp:+19122248996'
    )
    print(message.status)
    #print("Bring an Umbrella")
