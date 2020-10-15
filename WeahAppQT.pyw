# -*- coding: utf-8 -*-
#version PySide2 20201001
# dkpd-python3.5
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
                           QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import requests

url = 'http://api.openweathermap.org/data/2.5/weather'
api = '932d999dbd95894887b3ed90a9d65cc7'


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
            Form.setFixedSize(500, 468)
        Form.resize(500, 468)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 0, 161, 31))
        self.label.setStyleSheet(u"font-size: 14px;") #Панель ввыод на экран ввода города
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 30, 200, 25)) # Поле ввода города
        self.lineEdit.setStyleSheet(u"font-size: 14px;") # Поле ввода города
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 45, 390, 231)) #Панель информации вывод
        self.label_2.setStyleSheet(u"font-size: 14px;") #Панель информации вывод
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(223, 28, 75, 28)) #Кнопка
        self.pushButton.setStyleSheet(u"font-size: 17px;")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3") #Нижняя часть
        self.label_3.setGeometry(QRect(10, 430, 191, 31))
        self.label_3.setStyleSheet(u"font-size: 10px;")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(400, 420, 75, 25))
        self.pushButton_2.setStyleSheet(u"font-size: 14px;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"WeatherApp QT v.1.0", None))
        self.label.setText(QCoreApplication.translate("Form", u"Введите город:", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.label_3.setWhatsThis("")
        self.label_3.setText(QCoreApplication.translate("Form", u"TESTING", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0439\u0442\u0438", None))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./weather_icon/welcome.png'))


    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    def bp():
        s_city = ui.lineEdit.text()
        try:
            params = {'APPID': api, 'q': s_city, 'units': 'metric', 'lang':'RU' }
            result = requests.get(url, params=params)
            weather = result.json()

            if weather["main"]['temp'] < 10:
                state = "Сейчас холодно!"
            elif weather["main"]['temp'] < 20:
                state = "Сейчас прохладно!"
            elif weather["main"]['temp'] > 38:
                state = "Сейчас жарко!"
            else:
                state = "Сейчас отличная температура!"

            ui.label_2.setText("В городе " + str(weather["name"]) + " температура " + str(
                float(weather["main"]['temp'])) + " °C" + "\n" +
                               "Максимальная температура " + str(float(weather['main']['temp_max'])) + " °C" + "\n" +
                               "Минимальная температура " + str(float(weather['main']['temp_min'])) + " °C" + "\n" +
                               "Скорость ветра " + str(float(weather['wind']['speed'])) + "\n" +
                               "Давление " + str(round(weather['main']['pressure']* 0.750062)) + " мм рт. ст." +"\n" +
                               "Влажность " + str(float(weather['main']['humidity'])) + "\n" +
                               "Видимость " + str(weather['visibility']) + "\n" +
                               "Описание " + str(weather['weather'][0]["description"]) + "\n" + "\n" + state)

        except:
            ui.label_2.setText("Город " + s_city + " не найден")


def quit():
    sys.exit()


ui.pushButton.clicked.connect(bp)
ui.pushButton_2.clicked.connect(quit)

sys.exit(app.exec_())
