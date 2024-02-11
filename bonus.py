def input_weather_data(weather_dict):
    city = input("Enter the city name: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    temperature = input("Enter the temperature: ")
    humidity = input("Enter the humidity: ")
    weather_condition = input("Enter the weather condition: ")

    if city not in weather_dict:
        weather_dict[city] = {}
    weather_dict[city][date] = {
        'temperature': temperature,
        'humidity': humidity,
        'condition': weather_condition
    }
    print("Weather data added successfully!")


def query_by_city(weather_dict):
    city = input("Enter the city name to query: ")
    if city in weather_dict:
        print(f"Weather data for {city}:")
        for date, data in weather_dict[city].items():
            print(f"Date: {date}, Temperature: {data['temperature']}, 
                  Humidity: {data['humidity']}, Condition: {data['condition']}")
    else:
        print("City not found in the database.")


def main():
    weather = {}

    while True:
        print("1. Input Weather Data")
        print("2. Query by City")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            input_weather_data(weather)
        elif choice == '2':
            query_by_city(weather)
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

main()