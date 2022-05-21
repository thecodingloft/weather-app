import requests
from configparser import ConfigParser
import json
import pprint
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
# http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}

api_key = "865171f4a24aa1ebd3dc0f78dd5ed37a"


def _get_api_key():
    config = ConfigParser()
    config.read("secrets.ini")
    return config["openweather"]["api_key"]


def get_geodata(city, country):

    api_key = _get_api_key()

    r = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct?q={city},{country}&limit=1&appid={api_key}")
    response = r.json()

    lat = response[0]["lat"]
    lon = response[0]["lon"]

    return lat, lon


def get_weather(lat, lon):

    api_key = _get_api_key()

    r = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}")

    response = r.json()
    pprint.pprint(response)
    print("--- TODAY'S WEATHER ---")
    weather_description = response["weather"][0]["description"]

    print(weather_description)
    return weather_description


if __name__ == '__main__':
    location = get_geodata("Berlin", "DE")
    get_weather(location[0], location[1])
