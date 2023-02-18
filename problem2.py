import json
import time

import requests


def weather_data():
    url="https://api.openweathermap.org/data/2.5/weather?q=Dinajpur&appid=ab1fde35dfb0964d9b2818f71e7676d1"
    response = requests.get(url)
    content = response.content.decode('UTF-8')
    dict_content=json.loads(content)
    weather_info=dict_content['weather']
    while True:
        print(weather_info)
        time.sleep(3)

weather_data()
    