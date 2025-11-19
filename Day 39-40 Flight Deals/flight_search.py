import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv(".env")
AMADEUS_ENDPOINT = "https://test.api.amadeus.com/v1"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ.get("AMADEUS_API_KEY")
        self._api_secret = os.environ.get("AMADEUS_API_SECRET")
        self._token = self._get_new_token()

    def _get_new_token(self):
        TOKEN_ENDPOINT = "security/oauth2/token"

        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            'grant_type': 'client_credentials',
            'client_id':self._api_key,
            'client_secret': self._api_secret
        }
        
        response = requests.post(url=f"{AMADEUS_ENDPOINT}/{TOKEN_ENDPOINT}", headers=header, data=body)
        response.raise_for_status()
        token = response.json()['access_token']
        return token

    def get_destination_codes(self, city):
        CITIES_ENDPOINT = "reference-data/locations/cities"
        header = {"Authorization": f"Bearer {self._token}"}
        param  = {
            "keyword":city.upper(),
            "max": "2",
            "include":"AIRPORTS",
        }
        response = requests.get(url=f"{AMADEUS_ENDPOINT}/{CITIES_ENDPOINT}", headers=header, params=param)
        response.raise_for_status()
        data = response.json()["data"][0]
        code = data["iataCode"]
        return code
    
    def get_flights(self, origin_city_code, destination_city_code,from_time,to_time):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }

        response = requests.get(
            url=FLIGHT_ENDPOINT,
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("Response body:", response.text)
            return None

        return response.json()