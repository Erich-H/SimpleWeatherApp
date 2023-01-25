from tkinter import *
from tkinter import messagebox
import requests
import json
import config 
from datetime import datetime

# window_width = 800
# window_height =600
# # # creating the GUI
# root = Tk()
# root.geometry('800x600')
# root.resizable(0,0)
# root.title('Simple Weather App')


# city_name = StringVar()

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

        weather_now = f'Temperature: {temp}\n Feels like: {feels_like} \n Condition: {condition}'
        print(weather_now)


getWeather()


# city_header =Label(root, text='Enter City Name').pack(pady=10)
# city_input = Entry(root, textvariable=city_name, width=20).pack()


# btn = Button(root, text='Check Weather', command=getWeather)
# btn_width = btn.winfo_width()
# btn_height = btn.winfo_height()
# btn.place(x= (window_width - btn_width) / 2, y= (window_height - btn_height) / 2)
# root.mainloop()

