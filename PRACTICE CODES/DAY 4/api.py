from logging import exception

import requests


def weather(city, api_keys):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_id}"
    try:
     respose = requests.get(url)
     respose.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
     data = respose.json()
     temp = data["main"]["temp"]
     humidity = data["main"]["humidity"]
     feels_like = data["main"]["feels_like"]

     print(f"weather in {city}:")
     print(f"Temperature: {temp} celsius (feels like {feels_like} celsius)")
     print(f"Humidity: {humidity}%")
     print(f"description:{data["weather"][0]["description"].capitalize()}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from the API: {e}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    api_id = input("Enter your API key: ")
    weather(city, api_id)





