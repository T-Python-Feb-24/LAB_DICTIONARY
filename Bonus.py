
from datetime import datetime

weather_data = {}

def add_weather(city, date, temperature, humidity, condition):
    if city not in weather_data:
        weather_data[city] = {}
    weather_data[city][date] = {'temperature': temperature, 'humidity': humidity, 'condition': condition}

def search_weather(city):
    if city in weather_data:
        for date, data in weather_data[city].items():
            print(f"Weather data for {city}:")
            print(f"  - Date: {date}. \n  - Temperature: {data['temperature']}°C. \n  - Humidity: {data['humidity']}%. \n  - Condition: {data['condition']}.")
    else:
        print(f"No weather data found for {city}")

while True:
    print("-------- Choose an Option --------")
    print("1. Add Weather Data")
    print("2. Search Weather Data by City")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            city = input("Enter city name: ")
            date = datetime.strptime(input("Enter date (dd-mm-yyyy): "), "%d-%m-%Y").date()
            temperature = float(input("Enter temperature (°C): "))
            humidity = int(input("Enter humidity (%): "))
            condition = input("Enter weather condition: ")
            add_weather(city, date, temperature, humidity, condition)
        case 2:
            city = input("Enter city name: ")
            search_weather(city)
        case 3:
            print("----------------------------------")
            break
        case _:
            print("Invalid choice. Please try again.")