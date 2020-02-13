import requests

ID = "4fbea5e1e53b97856a45324e31b27a40"

class Location:

    def __init__(self, place):
        self.place = place
        self.request = requests.get("http://api.openweathermap.org/data/2.5/weather?q={:s}&appid={:s}".format(self.place,ID))
        self.r_json = self.request.json()
        self.weather = self.r_json['weather'][0]['main']
        self.humidity = self.r_json['main']['humidity']
        self.tempK = self.r_json['main']['temp']
        self.currentTemp = self.kelvinToFaren(self.tempK)
        self.windSpeed = self.r_json['wind']['speed']

    def __str__(self):
        myString = "Currently in {:s}:\nTemperature: {:.2f}\nWeather Conditions: {:s}\nHumidity Level: {:d}".format(self.place, self.currentTemp, self.weather\
        	,self.humidity)
        return myString

    @staticmethod   
    def kelvinToFaren(temp):
        farenheit = (temp - 273.15) * (9/5) + 32
        return farenheit

