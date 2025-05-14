import requests

def get_weather(city, api_key):
    """Fetch the current weather for a specified city."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        
        print(f"City: {data['name']}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Weather: {weather['description']}")
    else:
        print("City not found or API error.")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    get_weather(city_name, api_key)
