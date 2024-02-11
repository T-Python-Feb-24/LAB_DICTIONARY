# Weather Data Aggregation
from datetime import datetime

# dummy data
weather: dict = {"Jeddah": {
    "date": "23-02-2024",
    "temperature": 23,
    "humidity": 70,
    "condition": "sunny"

}}


def add_weather_data():
    weather.update({
        input("enter city name: ").capitalize(): {
            "date": get_weather_date(),
            "temperature": int(input("enter the temperature: ")),
            "humidity": int(input("enter the humidity: ")),
            "condition": str(input("enter the condition: ")),
        }})


def get_weather_date() -> str:
    while True:
        the_date = input("enter the date as dd-MM-yyyy: ")
        try:
            datetime.strptime(the_date, "%d-%m-%Y")
            return the_date
        except ValueError:
            print("invalid date")


def get_weather_data() -> None:
    city_name: str = input("Enter the city name:").capitalize()

    print(f"the weather for {city_name} is: \
{weather.get(city_name, "Not Found")}")


def delete_city() -> None:
    city_name: str = input("Enter the city name:").capitalize()
    weather.pop(city_name)
    print(f"the city weather info for {city_name} deleted successfully")


def menu_weather() -> int:
    try:
        choice: int = int(input('''
==================================================
1- Add or update weather data for a city:
2- Get weather data for a city:
3- Delete weather data for a city: 
q- Exit
--------------------------------------------------
enter your choice from (1-3) or \"q\" to exit: '''))
        return choice
    except ValueError:
        print("invalid input")


choice: int = 0
while True:
    choice = menu_weather()
    match choice:
        case 1:
            add_weather_data()

        case 2:
            get_weather_data()
        case 3:
            delete_city()
        case "q":
            exit()
        case _:
            print("please choose from (1-3): or \"q\" to exit")
            continue
