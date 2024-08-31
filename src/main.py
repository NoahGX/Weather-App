import requests

# Define main function
def main():
    # Read the API Key from a text file
    API_KEY = open("../data/api.txt", "r").read()
 
    # Prompt the user to enter a city name of their choosing
    user_input = input("Enter City Name: ")
    
    # Make an API request to get the URL
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={user_input}&units=imperial").json()
    
    # Print the results
    if weather_data['cod'] == "404":
        print("Invalid City Name.")
    else:
        print(weather_data)

# Main function
if __name__ == "__main__":
    main()