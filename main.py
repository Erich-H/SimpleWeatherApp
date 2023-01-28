import tkinter as tk
from tkinter import INSERT, StringVar
import requests
import json
import config 
from datetime import datetime


# # # creating the GUI
root = tk.Tk()
root.geometry('800x600')
root.resizable(0,0)
root.title('Simple Weather App')


city_val = StringVar()

# formats time per location
def time_format(utc):
    local_time = datetime.utcfromtimestamp(utc)
    return local_time.time()

# function for showing the weather
def getWeather():

    city_name = city_val.get()
    weather_url = 'https://api.openweathermap.org/data/2.5/weather?q='+ city_name +'&appid=' + config.api_key + '&units=imperial'
    print(weather_url)
  
    response = requests.get(weather_url)
    curr_weather = response.json()

    output.delete("1.0", "end")


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
        output.insert(INSERT, weather_now)
    else:
        weather_now = 'Please try another city name'
        output.insert(INSERT, weather_now)


header = tk.Label(root, text="Enter a city name").pack(pady=10)
city_input = tk.Entry(root, textvariable= city_val).pack()

btn = tk.Button(root, command=getWeather, text="Get Forecast").pack(pady=20)

weather = tk.Label(root, text="The Current Weather is: ").pack(pady=10)

output = tk.Text(root, width=46, height=10)
output.pack()
#mainloop for window
root.mainloop()
