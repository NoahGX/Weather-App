import requests

# Read the API Key from a text file
API_KEY = open("../data/api.txt", "r").read()
 
# Prompt the user to enter a city name of their choosing
user_input = input("Enter City Name: ")

# Make an API request to get the URL
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={user_input}&units=imperial")

# Print the results in JSON format
print(weather_data.json())