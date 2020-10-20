#windows version tkinter TWeather v: 1.1a
import tkinter as tk
import pyowm
import datetime, time


class WeatherInfo(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.wm_title('Weather')
        self.temp = tk.StringVar(self,value='')
        self.humid = tk.StringVar(self,value='')
        self.status = tk.StringVar(self,value='')
        self.sunrise = tk.StringVar(self,value='')
        self.sunset = tk.StringVar(self,value='')
        self.ld = tk.StringVar(self,value = '')
        self.ln = tk.StringVar(self,value = '')

        self.ask = tk.LabelFrame(self, text ='Location')
        self.ask.pack(fill='both',expand='yes')
        self.kw_label = tk.Label(self.ask, text ='Get weather in:')
        self.kw_label.pack(side = tk.LEFT)
        self.kw = tk.Entry(self.ask)
        self.kw.pack(side = tk.RIGHT)
        self.rb = tk.Button(self, text='Go', command = self.search)
        self.rb.pack()
        self.owm = pyowm.OWM('932d999dbd95894887b3ed90a9d65cc7')

        self.output = tk.LabelFrame(self, text ='Information')
        self.output.pack(fill='both',expand='yes')
        tk.Label(self.output, textvariable = self.temp).pack()
        tk.Label(self.output, textvariable=self.humid).pack()
        tk.Label(self.output, textvariable=self.status).pack()
        tk.Label(self.output, textvariable=self.sunrise).pack()
        tk.Label(self.output, textvariable=self.sunset).pack()
        tk.Label(self.output, textvariable=self.ld).pack()
        tk.Label(self.output, textvariable=self.ln).pack()
        button = tk.Button(master=self, text='Quit', command=self._quit)
        button.pack(side=tk.BOTTOM)

    def search(self):
        obs = self.owm.weather_at_place(self.kw.get())
        try:
            w = obs.get_weather()
            self.temp.set('Temperature: ' +str(round(w.get_temperature()['temp'] - 273.15,0))+ ' C')
            self.humid.set('Humidity: '+str(w.get_humidity())+ '%')
            self.status.set('Status: ' + w.get_status())
            self.sunrise.set('Sunrise at '+datetime.datetime.fromtimestamp(w.get_sunrise_time()).strftime('%H:%M:%s'))
            self.sunset.set('Sunset at '+datetime.datetime.fromtimestamp(w.get_sunset_time()).strftime('%H:%M:%s'))
            self.ld.set('Day length: '+str(round((w.get_sunset_time() - w.get_sunrise_time())/3600,1))+' h')
            self.ln.set('Night length: '+str(round(24 - (w.get_sunset_time() - w.get_sunrise_time())/3600,1))+' h')
        except:
            self.temp.set('Pick a city to display weather.')
    def _quit(self):
        self.quit()
        self.destroy()
app = WeatherInfo()
app.mainloop()