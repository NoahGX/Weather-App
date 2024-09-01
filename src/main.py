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
    dateTime = dt.datetime.fromtimestamp(weather_data['dt'], dt.timezone.utc)
    dateTime = dateTime + dt.timedelta(seconds=weather_data['timezone'])

    # Convert datetime objects to strings
    date = dateTime.strftime("%A, %b %-d %Y")
    time = dateTime.strftime("%I:%M:%S %p")
    
    # Handle errors
    if error:
        console.print(error, style="bold red")
        return
    else:
        # If there are no errors, print data
        console.print(f"[bold]{weather_data['name']}[/bold] Local Date: [bold green]{date}[/bold green]")
        console.print(f"[bold]{weather_data['name']}[/bold] Local Time: [bold green]{time}[/bold green]")
        console.print(f"\tCurrent Weather: "f"[bold cyan]{weather_data['weather'][0]['main']}[/bold cyan]")
        console.print(f"\tDescription: [bold cyan]{weather_data['weather'][0]['description']}[/bold cyan]")
        console.print(f"\tTemperature: {round(weather_data['main']['temp'])} ºF")
        console.print(f"\tIt Feels Like: {round(weather_data['main']['feels_like'])} ºF")
        console.print(f"\tPressure: {weather_data['main']['pressure']} hPa")
        console.print(f"\tHumidity: {weather_data['main']['humidity']} %")
        console.print(f"\tVisibility: {weather_data['visibility']} m")
        console.print(f"\tWind Speed: {weather_data['wind']['speed']} mph")

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