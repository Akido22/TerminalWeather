#windows version tkinter TWeather v: 1.1a
import tkinter as tk
import requests
from PIL import Image, ImageTk

App = tk.Tk()
App.title('Weather AppTK2 v.1.0')

HEIGHT = 500
WIDTH = 600

def format_response(weather_json):
    try:
        city = weather_json['name']
        conditions = weather_json['weather'][0]['description']
        temp = weather_json['main']['temp']
        wind = weather_json['wind']['speed']
        press = str(float(round(weather_json['main']['pressure']* 0.750062)))
        final_str = 'Город: %s \nConditions: %s \nTemperature (°C): %s \nTSpeed wind (m/s): %s \nPressure (hPa): %s' % (city, conditions, temp, wind, press)
    except:
        final_str = 'There was a problem retrieving that information'

    return final_str


def get_weather(city):
    weather_key = 'edffd1bf975a74d5d10e58c5ac8be2d3'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': '932d999dbd95894887b3ed90a9d65cc7', 'q': city, 'units':'metric', 'lang':'ru'}
    response = requests.get(url, params=params)
    print(response.json())
    weather_json = response.json()

    results['text'] = format_response(response.json())

    icon_name = weather_json['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon):
    size = int(lower_frame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./weather_icon/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img

C = tk.Canvas(App, height=HEIGHT, width=WIDTH)
background_image= tk.PhotoImage(file='./weather_icon/landscape.png')
background_label = tk.Label(App, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()

frame = tk.Frame(App,  bg='#42c2f4', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

textbox = tk.Entry(frame, font=40)
textbox.place(relwidth=0.65, relheight=1)

submit = tk.Button(frame, text='Проверить', font=40, command=lambda: get_weather(textbox.get()))

submit.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(App, bg='#42c2f4', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

bg_color = 'white'
results = tk.Label(lower_frame, anchor='nw', justify='left', bd=4)
results.config(font=40, bg=bg_color)
results.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(results, bg=bg_color, bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

App.mainloop()