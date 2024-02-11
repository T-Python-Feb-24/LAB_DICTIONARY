
def weather_data():
    weather_list= []
    while True:
        city = input("Enter the city name (or enter 'stop' to quit): ")
        if city == 'stop':
            break
        date = input("Enter the date: ")
        temperature = input("Enter the temperature: ")
        humidity = input("Enter the humidity: ")
        condition = input("Enter the weather condition: ")
        
        weather_entry = {
            'city': city,
            'date': date,
            'temperature': temperature,
            'humidity': humidity,
            'condition': condition
        }
        weather_list.append(weather_entry)
    return weather_list


def query_weather_data(weather_list):
    city = input("Enter the city name to query: ")
    found_data = False
    for entry in weather_list:
        if entry['city'] == city:
            print(f"Weather data for {city}:")
            print(f"Date: {entry['date']}")
            print(f"Temperature: {entry['temperature']}")
            print(f"Humidity: {entry['humidity']}")
            print(f"Weather Condition: {entry['condition']}")
            print()
            found_data = True
    
    if not found_data:
        print(f"No weather data found for {city}")

def main():
    weather_list = weather_data()
    query_weather_data(weather_list)

if __name__ == '__main__':
    main()