import requests
from collections import namedtuple
import json
import sys

#  # mozna uzyc slownika zamiast namedtuple
# Weather = namedtuple("Weather", ['location', 'temperature', 'air_pressure', 'humidity'])
#
# weather = Weather(
#     location = "Warszawa",
#     temperature = 25,
#     air_pressure= 1024,
#     humidity=80
# )
#
# print(weather.humidity)


Weather = namedtuple("Weather", ['location', 'temperature', 'air_pressure', 'humidity'])

def get_location_id(location_name):
    resp = requests.get(f'https://www.metaweather.com/api/location/search/?query={location_name}')
    return resp.json()[0]['woeid']

def get_location_weather(location_id):
    resp = requests.get(f"https://www.metaweather.com/api/location/{location_id}/").json()
    return Weather(
        location=resp['title'],
        temperature=resp['consolidated_weather'][0]['the_temp'],
        air_pressure=resp['consolidated_weather'][0]['air_pressure'],
        humidity=resp['consolidated_weather'][0]['humidity'],
    )

def print_weather(weather):
    result = f"""
Pogoda w {weather.location}:
 -temperatura {weather.temperature}
 -ciśnienie {weather.air_pressure}
 -wilgotność {weather.humidity}
"""
    print(result)

location_id = get_location_id("Berlin")
weather = get_location_weather(location_id)
print_weather(weather)


