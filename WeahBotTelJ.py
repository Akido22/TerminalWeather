import requests
import telebot
from datetime import datetime

url = 'http://api.openweathermap.org/data/2.5/weather'
api_weather = '932d999dbd95894887b3ed90a9d65cc7'
api_telegram = '1178695488:AAG9mtNhrs8ZNptgZyEUET5prGh2rjt5x9U'

bot = telebot.TeleBot(api_telegram)

@bot.message_handler(commands=['start'])
def welcome(message):
	#sti = open('welcome.png', 'rb')
	#bot.send_sticker(message.chat.id, sti)
	bot.send_message(message.chat.id, 'Добро пожаловать, ' + str(message.from_user.username) + ',' + '\n' +
	 'Введите название вашего города, для того чтобы узнать погоду!')


@bot.message_handler(content_types=['text'])
def weather_send(message):
	city = message.text
	try:
		params = {'APPID': api_weather, 'q': city, 'units': 'metric', 'lang': 'ru'}
		result = requests.get(url, params=params)
		weather = result.json()

		bot.send_message(message.chat.id, "По информации на " + str(datetime.now().strftime("%H:%M")) + ', в городе ' + str(weather["name"]) + " температура " + str(float(weather["main"]['temp'])) + "\n" +
				"Сегодня: Сейчас"
				"Максимальная температура " + str(float(weather['main']['temp_max'])) + "\n" +
				"Минимальная температура " + str(float(weather['main']['temp_min'])) + "\n" +
				"Скорость ветра " + str(float(weather['wind']['speed'])) + "\n" +
				"Давление " + str(float(round(weather['main']['pressure']* 0.750062))) + ' мм рт. ст.' + "\n" +
				"Влажность " + str(float(weather['main']['humidity'])) + "\n" +
				"Видимость " + str(weather['visibility']) + "\n" +
				"Описание " + str(weather['weather'][0]["description"]) + "\n")

		#if weather["main"]['temp'] < 10:
			#bot.send_message(message.chat.id, "Сейчас холодно!")
		#elif weather["main"]['temp'] < 20:
			#bot.send_message(message.chat.id, "Сейчас прохладно!")
		#elif weather["main"]['temp'] > 38:
			#bot.send_message(message.chat.id, "Сейчас жарко!")
		#else:
			#bot.send_message(message.chat.id, "Сейчас отличная температура!")

	except:
		bot.send_message(message.chat.id, "Извините, произошла ошибка")


if __name__ == '__main__':
	bot.polling(none_stop=True)