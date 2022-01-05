import requests
from django.conf import settings


def get_weather_data(city):
    temp = requests.get(
        'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + settings.WEATHER_API_KEY).json()
    return temp['main']['temp']
