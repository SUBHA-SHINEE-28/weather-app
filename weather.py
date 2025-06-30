import requests
from dotenv import load_dotenv
from pprint import pprint
import os


load_dotenv()


def get_current_weather(city="kansas city"):

    request_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={os.getenv("API_KEY")}&units=imperial'

    weather_data = requests.get(request_url).json()
    return weather_data


if __name__ == "__main__":
    print("\n*** Get Current Weather Conditions ***\n")

    city = input("\nEnter city: ")

    weather_data = get_current_weather(city)

    print("\n")
    print(weather_data)
