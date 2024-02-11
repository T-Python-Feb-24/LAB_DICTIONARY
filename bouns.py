# Initialize a global dictionary to store weather data
weather_data = {}

def input_weather():
    city = input("Enter city name: ").title()
    date = input("Enter date (YYYY-MM-DD): ")
    temperature = float(input("Enter temperature in Celsius: "))
    humidity = int(input("Enter humidity percentage: "))
    condition = input("Enter weather condition (e.g., Sunny, Rainy): ").capitalize()

    if city not in weather_data:
        weather_data[city] = {}
    weather_data[city][date] = {
        'temperature': temperature,
        'humidity': humidity,
        'condition': condition
    }
    print("Weather data added successfully.")

def query_by_city():
    city = input("Enter city name to query: ").title()
    if city in weather_data:
        print(f"Weather data for {city}:")
        for date, details in weather_data[city].items():
            print(f"  Date: {date}, Temperature: {details['temperature']}°C, Humidity: {details['humidity']}%, Condition: {details['condition']}")
    else:
        print("No data found for this city.")

def update_delete_data():
    city = input("Enter city name: ").title()
    date = input("Enter date (YYYY-MM-DD): ")
    
    if city in weather_data and date in weather_data[city]:
        action = input("Do you want to Update (U) or Delete (D) data? ").upper()
        if action == 'D':
            del weather_data[city][date]
            print("Data deleted successfully.")
        elif action == 'U':
            temperature = float(input("Enter new temperature in Celsius: "))
            humidity = int(input("Enter new humidity percentage: "))
            condition = input("Enter new weather condition (e.g., Sunny, Rainy): ").capitalize()
            weather_data[city][date] = {
                'temperature': temperature,
                'humidity': humidity,
                'condition': condition
            }
            print("Data updated successfully.")
        else:
            print("Invalid action selected.")
    else:
        print("No data found for the specified city and date.")

def main():
    while True:
        print("\nOptions:")
        print("1 - Input weather data")
        print("2 - Query weather data by city")
        print("3 - Update/Delete weather data")
        print("4 - Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            input_weather()
        elif choice == '2':
            query_by_city()
        elif choice == '3':
            update_delete_data()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
