weather_info = {
    "Riyadh":[{"date": "2020 1 8", "temperature": 45, "humidity": 10, "condition": "Sunny"}]


}

def input_data():
    ''' for enter weather data by the user'''
    city = input("Enter name of the city -> ")
    date = input("Enter date year-month-day -> ")
    temperature = float(input("Enter temperature (in Celsius) -> "))
    humidity = float(input("Enter humidity (in percentage) -> "))
    condition = input("Enter weather condition -> ")
    if city not in weather_info:
        weather_info[city] = []
    weather_info[city].append({"date": date, "temperature": temperature, "humidity": humidity, "condition": condition})
    print("Weather data added successfully.")

def city_weather():
    '''query weather data by city'''
    city = input("Enter city name to query: ")
    if city in weather_info:
        print(f"Weather data for {city}:")
        for entry in weather_info[city]:
            print(f"Date: {entry['date']}, Temperature: {entry['temperature']}, Humidity: {entry['humidity']}, Condition: {entry['condition']}")
    else:
        print("City not found in weather data.")

while True:
    print("1. Input weather data")
    print("2. Query weather by city")
    print("3. Exit")
    choice = input("Enter the number -> ")
    
    if choice == '1':
        input_data()
    elif choice == '2':
        city_weather()
    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
