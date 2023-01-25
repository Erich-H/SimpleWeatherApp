from tkinter import *
from tkinter import messagebox
import requests
import json
import config 
from datetime import datetime

# function for showing the weather
# def getWeather():
#     city_name = input('What city ? ')

#     units = ['Imperial', 'Metric']
#     print('What units do you use for temperature? ')
#     choice = input('1-Imperial or 2-Metric? > ')

#     if choice == '1':
#         weather_url = 'https://api.openweathermap.org/data/2.5/weather?q='+ city_name +'&appid=' + config.api_key + '&units' + units[int(choice) - 1]
#         print(weather_url)
#     elif choice == '2':
#         weather_url = 'https://api.openweathermap.org/data/2.5/weather?q='+ city_name +'&appid=' + config.api_key + '&units=' +units[int(choice) - 1]
#         print(weather_url)
    
#     response = requests.get(weather_url)
#     curr_weather = response.json()

#     # tfield.delete("1.0", 'end')


#     if curr_weather['cod'] == 200:
#         kelvin = 273 
#         #formatting the data and setting to variables
#         temp = int(curr_weather['main']['temp'] - kelvin) * (9 / 5) + 32
#         feels_like = int(curr_weather['main']['feels_like'] - kelvin) * (9 / 5) + 32
#         condition = curr_weather['weather'][0]['main']
#         weatherDisc = curr_weather['weather'][0]['description']
#         print(condition)
#         print(temp)
#         print(feels_like)
#         print(weatherDisc)
#         print(curr_weather)


# # getWeather()



window_width = 800
window_height =600
# # creating the GUI
root = Tk()
root.geometry('800x600')
root.resizable(0,0)
root.title('Simple Weather App')



btn = Button(root, text='Check Weather')
btn_width = btn.winfo_width()
btn_height = btn.winfo_height()
btn.place(x= (window_width - btn_width) / 2, y= (window_height - btn_height) / 2)
root.mainloop()