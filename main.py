import json
import csv

def extract_weather_to_csv(json_file, csv_file):
    """
    Извлекает информацию о температуре "feels_like" и погодных условиях "condition" по часам из JSON-файла 
    и записывает её в CSV-файл.

    :param json_file: Имя JSON-файла с данными о погоде.
    :param csv_file: Имя выходного CSV-файла.
    """
    try:
        # Открываем и читаем JSON-файл
        with open(json_file, 'r', encoding='utf-8') as f:
            weather_data = json.load(f)

        # Открываем CSV-файл для записи
        with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)

            # Записываем заголовки
            csv_writer.writerow(["Hour", "Feels Like (°C)", "Condition"])

            # Предполагаем, что данные по часам находятся в секции "hourly"
            hourly_data = weather_data.get("hourly", [])

            for hour_info in hourly_data:
                hour = hour_info.get("hour", "N/A")
                feels_like = hour_info.get("feels_like", "N/A")
                condition = hour_info.get("condition", "N/A")

                # Записываем строку в CSV-файл
                csv_writer.writerow([hour, feels_like, condition])

        print(f"Данные успешно записаны в файл {csv_file}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Использование функции
json_file = 'Amsterdam24.09.06.json'  # Имя JSON-файла
csv_file = 'Amsterdam_weather.csv'  # Имя выходного CSV-файла
extract_weather_to_csv(json_file, csv_file)
