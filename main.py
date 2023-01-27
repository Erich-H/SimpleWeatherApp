import tkinter as tk
from tkinter import messagebox
import requests
import json
import config 
from datetime import datetime


# # # creating the GUI
root = tk.Tk()
root.geometry('800x600')
root.resizable(0,0)
root.title('Simple Weather App')


# city_name = StringVar()

# formats time per location
def time_format(utc):
    local_time = datetime.utcfromtimestamp(utc)
    return local_time.time()

# function for showing the weather
def getWeather():

    city_name = input('Enter City Name ')
    weather_url = 'https://api.openweathermap.org/data/2.5/weather?q='+ city_name +'&appid=' + config.api_key + '&units=imperial'
    print(weather_url)
  
    response = requests.get(weather_url)
    curr_weather = response.json()

    # tfield.delete("1.0", 'end')


    if curr_weather['cod'] == 200:
        #formatting the data and setting to variables
        temp = int(curr_weather['main']['temp'])
        feels_like = int(curr_weather['main']['feels_like'])
        condition = curr_weather['weather'][0]['main']
        weatherDisc = curr_weather['weather'][0]['description']
        pressure = curr_weather['main']['pressure']
        humidity = curr_weather['main']['humidity']
        timezone = curr_weather['timezone']
        sunRise =time_format(curr_weather['sys']['sunrise'] + timezone)
        sunSet = time_format(curr_weather['sys']['sunset'] + timezone)
        

        weather_now = f'''Temperature: {temp} F\n Feels like: {feels_like} F \n Condition: {condition}
        Description: {weatherDisc}
        Pressure: {pressure}
        Humidity: {humidity}
        Sunrise: {sunRise}
        Sunset: {sunSet}'''
        print(weather_now)
    else:
        weather_now = 'Please try another city name'
        print(weather_now)

# test API call
# getWeather()


city_val = tk.Label(text="Enter a city name ")
entry = tk.Entry()
city_val.pack()
entry.pack()
#mainloop for window
root.mainloop()
