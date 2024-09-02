import requests
from rich.console import Console
from rich.table import Table
from rich import box
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

    # Return the data response
    return data_response

# Define function to display the weather data
def display_weather(weather_data):
    # Define the date and time
    dateTime = dt.datetime.fromtimestamp(weather_data['dt'], dt.timezone.utc)
    dateTime = dateTime + dt.timedelta(seconds=weather_data['timezone'])

    # Convert datetime objects to strings
    date = dateTime.strftime("%A, %b %-d %Y")
    time = dateTime.strftime("%I:%M:%S %p")

    # Assign variables for cleaner code
    city = weather_data['name']
    weather = weather_data['weather'][0]['main']
    description = weather_data['weather'][0]['description']
    temperature = round(weather_data['main']['temp'])
    feels_like = round(weather_data['main']['feels_like'])
    pressure = weather_data['main']['pressure']
    humidity = weather_data['main']['humidity']
    visibility = weather_data['visibility']
    wind_speed = weather_data['wind']['speed']

    # If there are no errors, print data
    console.print(f"[bold]{city}[/bold] Local Date: [bold green]{date}[/bold green]")
    console.print(f"[bold]{city}[/bold] Local Time: [bold green]{time}[/bold green]")
    console.print(f"\tCurrent Weather: "f"[bold cyan]{weather}[/bold cyan]")
    console.print(f"\tDescription: [bold cyan]{description}[/bold cyan]")
    console.print(f"\tTemperature: {temperature} ºF")
    console.print(f"\tIt Feels Like: {feels_like} ºF")
    console.print(f"\tPressure: {pressure} hPa")
    console.print(f"\tHumidity: {humidity} %")
    console.print(f"\tVisibility: {visibility} m")
    console.print(f"\tWind Speed: {wind_speed} mph")
    console.print(table)

# Define main function
def main():
    try:
        # Read the API Key from a text file
        with open("../data/api.txt", "r") as file:
            API_KEY = file.read()

        # Prompt the user to enter a city name of their choosing
        user_input = input("Enter City Name: ")
        
        # Call function to make an API request for weather data
        weather_data = fetch_weather(API_KEY, user_input)

        # Error Handling
        if weather_data['cod'] == '404':
            raise ValueError(weather_data['message'])

    except FileNotFoundError as file_err:
        console.print(f"File Error: {file_err}", style="bold red")
    except ValueError as api_err:
        console.print(f"API Error: {api_err}", style="bold red")
    except requests.exceptions.RequestException as net_err:
        console.print(f"Network Error: {net_err}", style="bold red")
    except Exception as err:
        console.print(f"Error: {err}", style="bold red")
        
    else:
        # Call the function to display the weather data
        display_weather(weather_data)

# Main function
if __name__ == "__main__":
    main()