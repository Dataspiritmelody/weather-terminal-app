import requests
import os
from dotenv import load_dotenv
class City:
    def __init__(self,name,lat,lon,units="metric"):
        self.name = name
        self.lat = lat
        self.lon =lon
        self.units = units
        # make an api call to get the weather information
        self.get_data()

    def get_data(self):
        try:
            load_dotenv()

            apiKey = os.getenv('OPEN_WEATHER_API')
            url = os.getenv('OPEN_WEATHER_URL')

            response =requests.get(f"{url}?units={self.units}&lat={self.lat}&lon={self.lon}&appid={apiKey}")
        except:
            print("No internet")
           
        self.response_json =response.json()
        self.temp= self.response_json["main"]["temp"]
        self.temp_min =self.response_json["main"][ "temp_min"]
        self.temp_max = self.response_json["main"]["temp_max"]

    def temp_print(self):
        units_symbol = "C"
        if self.units =="imperial":
            units_symbol = "F"

        print(f"In {self.name} it is currently {self.temp}°{units_symbol} ")
        print(f"Today low:{self.temp_min}°{units_symbol}")
        print(f"Today's High:{self.temp_max}°{units_symbol}")

city = input('Enter city name: ')
long = input('Enter city longitude: ')
lat = input('Enter city latitude: ')

customCity = City(city, long, lat)
customCity.temp_print()

# my_city = City("Tokyo",35.6897,139.6922)
# my_city.temp_print()

# vacation_city = City("portland",45.5152,-122.6784)
# vacation_city.temp_print()

# print(vacation_city.response_json)
