# 1.Ввод названия города с консольного ввода


import requests

# Ввод названия города с клавиатуры
city = input("Введите название города: ")

# API ключ для доступа к OpenWeatherMap (зарегистрируйтесь на сайте и вставьте свой ключ)
API_KEY = "79d1ca96933b0328e1c7e3e7a26cb347"

# Формируем URL для запроса
# units=metric - температура в градусах Цельсия
# lang=ru - описание погоды на русском языке
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"

# Отправляем GET-запрос и получаем ответ в формате JSON
data = requests.get(url).json()

# Извлекаем нужные данные из ответа
temp = data['main']['temp']              # температура
feels_like = data['main']['feels_like']  # ощущается как
pressure = data['main']['pressure']      # давление в гПа
humidity = data['main']['humidity']      # влажность в процентах
description = data['weather'][0]['description']  # описание погоды
wind = data['wind']['speed']             # скорость ветра в м/с

# Выводим информацию на экран
print(f"\nПогода в городе {city}:")
print(f"Температура: {temp}°C")
print(f"Ощущается как: {feels_like}°C")
print(f"Давление: {pressure} гПа")
print(f"Влажность: {humidity}%")
print(f"Ветер: {wind} м/с")
print(f"Описание: {description}")