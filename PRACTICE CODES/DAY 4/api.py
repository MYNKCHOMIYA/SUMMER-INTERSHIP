from logging import exception

import requests
from tornado.web import url


def weather(city, api_keys):
    url = "https://api.openweathermap.org/data/2.5/weather?q= {city}&appid= {api id}"

try:
    respose = requests.get(url)
    data = respose.json()

except requests.exceptions.RequestException as e:
  print(f"Error fetching data from OpenWeather data: {e}")

  city = input("Enter city name: ")
 api_keys = input("Enter your API key")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_keys}"



