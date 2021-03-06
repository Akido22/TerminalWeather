# -*- coding: utf-8 -*-
# Console version TWeather v: 1.2a
import pyowm  #PyOWM 2.10
from colorama import * # colorama
from datetime import datetime

owm = pyowm.OWM('932d999dbd95894887b3ed90a9d65cc7', language='RU')  #You API key OWM

print('----------------Console version: 1.2.6477----------------------')
print(Fore.LIGHTGREEN_EX + 'Здравствуйте, это программа на Python 3 и библиотеки PyOWM 2.10.\nОна поможет вам узнать погоду в любом городе, который выберите.\nПожалуйста, введите название вашего города.Удачи!\n')
city = input("Город: ")
print()

observation = owm.weather_at_place(city)
weather = observation.get_weather()
location = observation.get_location()

def azimuth_wind():
    if 337.5 < weather.get_wind()['deg'] <= 22.5:
        return 'Северный'
    if 157.5 < weather.get_wind()['deg'] <= 202.5:
        return 'Южный'
    if 67.5 < weather.get_wind()['deg'] <= 112.5:
        return 'Восточный'
    if 247.5 < weather.get_wind()['deg'] <= 292.5:
        return 'Западный'
    if 22.5 < weather.get_wind()['deg'] <= 67.5:
        return 'Северо-Восточный'
    if 112.5 < weather.get_wind()['deg'] <= 157.5:
        return 'Юго-Восточный'
    if 202.5 < weather.get_wind()['deg'] <= 247.5:
        return 'Юго-Западный'
    if 292.5 < weather.get_wind()['deg'] <= 337.5:
        return 'Северо-Западный'
    if weather.get_wind()['deg'] == 360:
        return 'Северный'

print('По информации на  ' + str(datetime.now().strftime("%H:%M")) + ', в городе ' + city + '.')
print('Сегодня: Сейчас '+str(weather.get_detailed_status() + '. Температура воздуха ' + str(weather.get_temperature('celsius')["temp"]) + ' °C,'))
print('ожидаемая максимальная температура воздуха сегодня ' + str(weather.get_temperature('celsius')["temp_max"]) + ' °C.' + '\n')

print('Влажность: ' + str(weather.get_humidity()) + ' %')
print('Ветер: ' + str(weather.get_wind()["speed"]) + ' м/с')
print('Направление ветра: ' + azimuth_wind())
print('Давление: ' + str(round(weather.get_pressure()['press'] * 0.750062)) + ' мм рт. ст.')
print('Видимость: ' + str(weather.get_visibility_distance()) + ' м.')
