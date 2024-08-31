import requests
from rich.console import Console

# Initialize console
console = Console()

# Define validation function
def weather(API_KEY, user_input):
    # Make an API request to get the URL
    data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={user_input}&units=imperial")
    
    # Ensure data is in JSON
    data = data.json()

    # Return weather data
    if data['cod'] == '404':
        return 'error'
    else:
        return data

# Define function to display weather data
def display(weather_data):
    # Handle errors in the API request
    if 'error' in weather_data:
        console.print("Invalid City Name.", style="bold red")
        return
    else: 
        # If there are no errors, print data
        console.print(weather_data)

# Define main function
def main():
    # Read the API Key from a text file
    API_KEY = open("../data/api.txt", "r").read()
 
    # Prompt the user to enter a city name of their choosing
    user_input = input("Enter City Name: ")
    
    # Make an API request to get the URL for weather data
    weather_data = weather(API_KEY, user_input)

    # Display the weather data
    display(weather_data)

# Main function
if __name__ == "__main__":
    main()