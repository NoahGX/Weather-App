import requests
from rich.console import Console

# Initialize console
console = Console()

# Define validation function
def weather_data(API_KEY, user_input):
    # Make an API request to get the URL
    data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={user_input}&units=imperial")
    
    # Ensure data is in JSON
    data = data.json()

    # Return weather data
    if data['cod'] == '404':
        return None, "Invalid City Name."
    else:
        return data, None

# Define main function
def main():
    # Read the API Key from a text file
    API_KEY = open("../data/api.txt", "r").read()
 
    # Prompt the user to enter a city name of their choosing
    user_input = input("Enter City Name: ")
    
    # Make an API request to get the URL
    weather, error = weather_data(API_KEY, user_input)

    # Handle errors in the API request
    if error:
        console.print(error, style="bold red")
        return
    else: 
        # If there are no errors, print data
        console.print(weather)

# Main function
if __name__ == "__main__":
    main()