import requests
from rich.console import Console

# Initialize console
console = Console()

# Define function to fetch the weather data
def fetch_weather(API_KEY, user_input):
    # Make an API request for the URL
    data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={user_input}&units=imperial")
    
    # Ensure data is in JSON
    data = data.json()

    # If there are no errors, return the data
    if data['cod'] == '404':
        return None, data['message']
    else:
        return data, None

# Define function to display the weather data
def display_weather(weather_data, error):
    # Handle errors in the API request
    if error:
        console.print(error, style="bold red")
        return
    else:
        # If there are no errors, print the data
        console.print(f"displaying data...", style="bold green")
        console.print(f"The current weather in {weather_data['name']} reads: {weather_data['weather'][0]['main']}")
        console.print(f"The temperature is: {weather_data['main']['temp']}")
        console.print(f"It currently feels like: {weather_data['main']['feels_like']}")
        console.print(f"The pressure is: {weather_data['main']['pressure']}")
        console.print(f"The humidity is: {weather_data['main']['humidity']}")
        console.print(f"The wind speed is: {weather_data['wind']['speed']} m/s, with gusts of {weather_data['wind']['gust']} m/s")

# Define main function
def main():
    # Read the API Key from a text file for current weather data
    API_KEY = open("../data/api.txt", "r").read()

    # Prompt the user to enter a city name of their choosing
    user_input = input("Enter City Name: ")
    
    # Call function to make an API request for the URL
    weather_data, error = fetch_weather(API_KEY, user_input)

    # Call function to display the weather data
    display_weather(weather_data, error)

# Main function
if __name__ == "__main__":
    main()