#!/usr/bin/python3
import subprocess
try:
    import requests
except ImportError:
    print("Requests library not found. Installing...")
    subprocess.check_call(["pip", "install", "requests"])
    import requests

def get_weather(city):
    # Create the URL
    url = f'https://goweather.herokuapp.com/weather/{city}'

    # Send the request
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            print(data["temperature"])
            return data
        except Exception as e:
            print(f"Error parsing JSON data: {e}")
            return None
    else:
        print(f"Request to the weather service failed with status code: {response.status_code}")
        return None

def get_weather_details(data, details):
    weather_info = {}

    if 'temperature' in details:
        weather_info['Temperature'] = f"{data['temperature']}"
    if 'wind' in details:
        weather_info['Wind'] = f"{data['wind']}"
    return weather_info

if __name__ == "__main__":
    city = input("Enter the city name: ")
    details = input("Enter the weather details you want ( wind,temperature): ").split(',')

    weather_data = get_weather(city)

    if weather_data:
        selected_weather_details = get_weather_details(weather_data, details)
        print(f"Weather information for {city}:")
        for key, value in selected_weather_details.items():
            print(f"{key}: {value}")
    else:
        print(f"City not found or an error occurred.")