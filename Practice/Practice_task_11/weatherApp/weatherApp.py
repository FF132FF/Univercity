import re
import ssl
import urllib.request
from datetime import datetime


def Time():
    now: function = datetime.now()
    currentTime: str = now.strftime("[%H:%M:%S]")
    return currentTime


ssl._create_default_https_context: str = ssl._create_unverified_context
selectedCity = str(input("enter the name of the city: "))
url: str = ("https://api.openweathermap.org/data/2.5/weather?q=" + selectedCity
            + "&units=metric&lang=ru&appid=c341e34f9b7c327502cde34aa7817c5f")
response: str = urllib.request.urlopen(url).read().decode()
logFile: str = "logFile.txt"


def requestLog(requestedFile: str, requestedData: str):
    content: TextIOWrapper = open(requestedFile, "a", encoding='utf-8')

    content.write(Time())

    cityPattern: str = r"(?:\"name\"\:\")([^\"}]*)"
    city: list = re.findall(cityPattern, requestedData)
    city: str = ''.join(city)
    content.write(f" Запрос погоды в городе: {city}")

    tempPattern: str = r"(?:\"temp\"\:)([^\.]*)"
    temp: list = re.findall(tempPattern, requestedData)
    temp: str = ''.join(temp)
    mainStatePattern: str = r"(?:\,\"description\"\:\")([^\"]*)"
    mainState: list = re.findall(mainStatePattern, requestedData)
    mainState: str = ''.join(mainState)
    content.write(f"\nТемпература: {temp}\u00b0C, {mainState}")

    airHumidityPattern: str = r"(?:\"humidity\"\:)([^\D]*)"
    airHumidity: list = re.findall(airHumidityPattern, requestedData)
    airHumidity: str = ''.join(airHumidity)
    content.write(f"\nВлажность воздуха: {airHumidity}%")

    windSpeedPattern: str = r"(?:\"speed\"\:)([^\D}]*)"
    windSpeed: list = re.findall(windSpeedPattern, requestedData)
    windSpeed: str = ''.join(windSpeed)
    content.write(f"\nСкорость ветра: {windSpeed} м/с")

    atmospherePressurePattern: str = r"(?:\"pressure\"\:)([^\D}]*)"
    atmospherePressure: list = re.findall(atmospherePressurePattern,
                                          requestedData)
    atmospherePressure: str = ''.join(atmospherePressure)
    content.write(f"\nАтмосферное давление: {atmospherePressure} мм рт. ст.")

    content.write("\n  ===========\n")
    content.close()


requestLog(logFile, response)