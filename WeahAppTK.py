# -*- coding: utf-8 -*-
# windows version tkinter 20201001
import requests
from tkinter import *
from tkinter import messagebox
from datetime import datetime

api_key = "932d999dbd95894887b3ed90a9d65cc7"

def proceed():
    city = cit.get()
    if city == '':
        return messagebox.showerror('Error', 'Enter City Name')
    else:
        owm_url = "http://api.openweathermap.org/data/2.5/weather?"
        cityname = city
        url = owm_url + "appid=" + api_key + "&q=" + cityname
        params = {'lang': 'ru', 'units':'metric'}
        response = requests.get(url, params=params)
        weather = response.json()


        def azimuth_wind():
            if 337.5 < weather['wind']['deg'] <= 22.5:
                return 'Северный'
            if 157.5 < weather['wind']['deg'] <= 202.5:
                return 'Южный'
            if 67.5 < weather['wind']['deg'] <= 112.5:
                return 'Восточный'
            if 247.5 < weather['wind']['deg'] <= 292.5:
                return 'Западный'
            if 22.5 < weather['wind']['deg'] <= 67.5:
                return 'Северо-Восточный'
            if 112.5 < weather['wind']['deg'] <= 157.5:
                return 'Юго-Восточный'
            if 202.5 < weather['wind']['deg'] <= 247.5:
                return 'Юго-Западный'
            if 292.5 < weather['wind']['deg'] <= 337.5:
                return 'Северо-Западный'
            if weather['wind']['deg'] == 360:
                return 'Северный'



        if weather["cod"] != "404":
            Label(App, text='По информации на ' + str(datetime.now().strftime("%H:%M")) + ', в городе ' + city + '.', font='Arial 8 bold').place(x=2, y=55)
            Label(App, text='Сейчас ' + str(weather['weather'][0]["description"]) + '. Температура воздуха ' + str(float(weather['main']['temp'])) + ' °C,', font='Helvetica 8 bold').place(x=2, y=75)
            Label(App, text='Температура воздуха максимальная ' + str(float(weather['main']['temp_max'])) + ' °C', font='Helvetica 8 bold').place(x=2, y=95)
            Label(App, text='Температура воздуха минимальная ' + str(float(weather['main']['temp_min'])) + ' °C', font='Helvetica 8 bold').place(x=2, y=115)
            Label(App, text='Скорость ветра ' + str(float(weather['wind']['speed'])) + ' м/с, Направление ветра ' + azimuth_wind(), font='Helvetica 8 bold').place(x=2, y=135)
            Label(App, text='Давления воздуха  ' + str(float(round(weather['main']['pressure']* 0.750062))) + ' мм рт. ст.', font='Helvetica 8 bold').place(x=2, y=155)
            Label(App, text='Влажность воздуха ' + str(float(weather['main']['humidity'])) + ' %' , font='Helvetica 8 bold').place(x=2, y=175)
            #Label(App,get(icon_id)).place(x=2, y=200)


        else:
            return messagebox.showerror('Error', 'No City Found')


App = Tk()
App.geometry('400x400')
App.title('Weather AppTK v.1.0')

cit = StringVar()

Label(App, text='Weather App INDX', font='Helvetica 10 bold').place(x=100, y=2)
Label(App, text='Город: ', font='Helvetica 10 bold').place(x=2, y=29)

Entry(App, width=17, textvariable=cit).place(x=50, y=29)
Button(App, text='Поиск',width=12, height = 1, command=proceed).place(x=158, y=25)

App.mainloop()
