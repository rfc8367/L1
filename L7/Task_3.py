import requests
import datetime
import json

APIID = "f9ada9efec6a3934dad5f30068fdcbb8"


def parameters():
    q = input('Введите город: ')
    cnt = input('Введите количество дней: ')
    return q, cnt


def url_link(q, cnt):
    response = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily?',
                            params={'q': q, 'cnt': cnt, 'units': 'metric', 'appid': APIID}).json()
    data = response.json()
    return data


def weather_forecast(data):
    with open('19-09-2020-Odessa-5-days-weather-forecast.txt', 'w') as file:

        file.write('Дата:   Температура днем:   Температура ночью:   По ощущениям днём:    По ощущениям ночью:   ')

        for i in data['list']:
            file.write(str(datetime.datetime.fromtimestamp(i['dt']).strftime("%d-%m-%Y")))
            file.write(str(i['temp']['day']) + 'temp_day')
            file.write(str(i['temp']['night']) + 'temp_night')
            file.write(str(i['feels_like']['day']) + 'felling_day')
            file.write(str(i['feels_like']['night']) + 'felling_night')
        file.close()

q, cnt = parameters()
data = url_link(q, cnt)
weather_forecast(data)