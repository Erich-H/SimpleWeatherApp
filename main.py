from tkinter import *
import requests
import json
import config 
from datetime import datetime



#creating the GUI
# root = Tk()
# root.geometry('800x600')
# root.resizable(0,0)
# root.title('Simple Weather App')






# function for showing the weather
def Weather():
    city_name = input('What city ? ')

    units = ['Imperial', 'Metric']
    print('What units do you use for temperature? ')
    choice = input('1-Imperial or 2-Metric? > ')

    if choice == '1':
        weather_url = 'https://api.openweathermap.org/data/2.5/weather?q='+ city_name +'&appid=' + config.api_key + '&units' + units[int(choice) - 1]
        print(weather_url)
    elif choice == '2':
        weather_url = 'https://api.openweathermap.org/data/2.5/weather?q='+ city_name +'&appid=' + config.api_key + '&units=' +units[int(choice) - 1]
        print(weather_url)
    
    response = requests.get(weather_url)
    curr_weather = response.json()

    # tfield.delete("1.0", 'end')


    if curr_weather['cod'] == 200:
        kelvin = 273 
        #formatting the data and setting to variables
        temp = int(curr_weather['main']['temp'])
        condition = curr_weather['main']['pressure']
        city_loc = curr_weather['coord']['lon']
        weatherDisc = curr_weather['weather'][0]['description']
        print(condition)
        print(city_loc)
        print(weatherDisc)
        print(curr_weather)


Weather()