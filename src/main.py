import requests
from rich.console import Console
import datetime as dt

# Initialize console
console = Console()

# Define function to fetch data for weather information
def fetch_weather(API_KEY, user_input):
    # Fetch URL to make an API request for current data
    URL = f"https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={user_input}&units=imperial"

    # Make an HTTP request to the URL to recieve data
    data_response = requests.get(URL)
    
    # Parse the JSON response
    data_response = data_response.json()

    # Proceed if there are no errors in the response
    if data_response['cod'] == '404':
        return None, data_response['message']
    else:
        return data_response, None

# Define function to display the weather data
def display_weather(weather_data, error):
    # Define the date and time
    dateTime = dt.datetime.fromtimestamp(weather_data['dt'], dt.UTC)

    # Handle errors
    if error:
        console.print(error, style="bold red")
        return
    else:
        # If there are no errors, print data
        console.print(f"displaying data...", style="bold green")
        console.print(f"The current weather in [bold]{weather_data['name']}[/bold] reads: "
                      f"[cyan bold]{weather_data['weather'][0]['main']}[/cyan bold], "
                      f"[cyan bold]{weather_data['weather'][0]['description']}[/cyan bold]")
        console.print(f"The temperature is: {round(weather_data['main']['temp'])} ºF")
        console.print(f"It currently feels like: {round(weather_data['main']['feels_like'])} ºF")
        console.print(f"The pressure is: {weather_data['main']['pressure']} hPa")
        console.print(f"The humidity is: {weather_data['main']['humidity']} %")
        console.print(f"The visibility is: {weather_data['visibility']} m")
        console.print(f"The wind speed is: {weather_data['wind']['speed']} mph")
        console.print(f"The Coordinated Universal Time (UTC) of this data is: {dateTime}")

# Define main function
def main():
    # Read the API Key from a text file
    with open("../data/api.txt", "r") as file:
        API_KEY = file.read()

    # Prompt the user to enter a city name of their choosing
    user_input = input("Enter City Name: ")
    
    # Call function to make an API request for weather data
    weather_data, error = fetch_weather(API_KEY, user_input)

    # Call the function to display the weather data
    display_weather(weather_data, error)

# Main function
if __name__ == "__main__":
    main()