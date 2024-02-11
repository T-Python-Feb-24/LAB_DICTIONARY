def input_weather_data()->dict:
    '''
    Function to input weather data
    '''
    weather_data = {}
    while True:
        city = input("Enter city name (or type 'done' to finish): ").strip().capitalize()
        if city.lower() == 'done':
            break
        date = input("Enter date (YYYY-MM-DD): ").strip()
        temperature = input("Enter temperature (in Celsius): ").strip()
        humidity = input("Enter humidity (%): ").strip()
        condition = input("Enter weather condition: ").strip().capitalize()

        if city not in weather_data:
            weather_data[city] = []
        weather_data[city].append({'date': date, 'temperature': temperature, 'humidity': humidity, 'condition': condition})

    return weather_data

def query_weather_by_city(weather_data, city):
    """
    Function to query weather data
    """
    if city in weather_data:
        print(f"Weather data for {city}:")
        for entry in weather_data[city]:
            print(f"Date: {entry['date']}, Temperature: {entry['temperature']}°C, Humidity: {entry['humidity']}%, Condition: {entry['condition']}")
    else:
        print("No weather data available for this city.")

def main():
    '''
    function to run the program.
    '''
    weather_data = input_weather_data()

    while True:
        city = input("Enter city name to query (or type 'done' to exit): ").strip().capitalize()
        if city.lower() == 'done':
            break
        query_weather_by_city(weather_data, city)

if __name__ == "__main__":
    main()
    
