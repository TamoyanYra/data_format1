import json
import csv

# Задаем имя JSON-файла и выходного CSV-файла
json_file = 'Amsterdam24.09.06.json'
csv_file = 'Amsterdam_weather.csv'

# Чтение данных из JSON-файла
with open(json_file, 'r') as file:
    data = json.load(file)

# Предполагается, что данные о погоде хранятся в формате списка по часам
# Например, data['hourly'] содержит список с данными о погоде
hourly_data = data.get('hourly', [])

# Открытие CSV-файла для записи
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Запись заголовков в CSV-файл
    writer.writerow(['Time', 'Feels Like (°C)', 'Condition'])

    # Запись данных по часам
    for hour in hourly_data:
        time = hour.get('time')  # Предположим, время хранится в hour['time']
        feels_like = hour.get('feels_like')  # Температура "как ощущается"
        condition = hour.get('condition')  # Погодные условия

        writer.writerow([time, feels_like, condition])

print(f"Данные успешно записаны в файл {csv_file}")
