import requests

# OpenWeatherMap API URL
api_url = "http://api.openweathermap.org/data/2.5/weather"

# Replace this with your actual API key
api_key = "01a76afcc7693fd425d5bb35b2223fc8"

# City Name (e.g., Kathmandu, Nepal)
city = "Kathmandu,NP"

# Parameters to send with the request
params = {
    "q": city,
    "appid": api_key,
    "units": "metric",  # Use "metric" for Celsius, "imperial" for Fahrenheit
}

# Making the API call
response = requests.get(api_url, params=params)

# Check if the response is successful
if response.status_code == 200:
    # Parse the response to JSON
    data = response.json()

    # Extract required information
    city_name = data["name"]
    weather_description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind_speed = data["wind"]["speed"]

    # Display the weather information
    print(f"Weather Forecast for {city_name}:")
    print(f"Weather: {weather_description.capitalize()}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure} hPa")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print("Error: Unable to fetch the weather data.")
    print(f"Response Code: {response.status_code}, Message: {response.text}")
