weather_data = {}

def add_weather_data():
    city = input("Enter the city name: ")
    date = input("Enter the date: ")
    temperature = validate_float_input("Enter the temperature: ")
    humidity = validate_float_input("Enter the humidity: ")
    condition = input("Enter the weather condition: ")
    #not finished yet