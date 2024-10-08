import os
import requests
import datetime as dt
from dotenv import load_dotenv
from flask import Flask, render_template, request

# Use environment variable for API Key storage
load_dotenv(dotenv_path='../config/.env')
API_KEY = os.getenv('API_KEY')

# Intitialize flask app
app = Flask(__name__, template_folder='../templates')

# Define function to fetch weather data from the API
def fetch_weather(API_KEY, user_input):
    # Fetch URL to make an API request
    URL = f"https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={user_input}&units=imperial"

    # Make an HTTP request to the API get the data
    data_response = requests.get(URL)
    
    # Parse the JSON response
    data_response = data_response.json()

    # Return the data
    return data_response

# Define function to display the weather data
def display_weather(weather_data):
    # Calculate the local date and time based on timezone
    dateTime = dt.datetime.fromtimestamp(weather_data['dt'], dt.timezone.utc)
    dateTime = dateTime + dt.timedelta(seconds=weather_data['timezone'])

    # Convert datetime objects to strings
    local_date = dateTime.strftime("%A, %b %-d %Y")
    local_time = dateTime.strftime("%I:%M:%S %p")

    # Extract details from the weather data
    weather_data = {
        'city': weather_data['name'],
        'country': weather_data['sys']['country'],
        'local_date': local_date,
        'local_time': local_time,
        'weather': weather_data['weather'][0]['main'],
        'description': weather_data['weather'][0]['description'],
        'temperature': round(weather_data['main']['temp']),
        'feels_like': round(weather_data['main']['feels_like']),
        'pressure': weather_data['main']['pressure'],
        'humidity': weather_data['main']['humidity'],
        'visibility': weather_data['visibility'],
        'wind_speed': weather_data['wind']['speed']
    }
    return weather_data

# Define flask route for home page
@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    err_message = None
    
    # Ensure API Key exists in the environment
    if not API_KEY:
        err_message = f"Value Error: API key not found"
        render_template('index.html', error=err_message)
    
    # Check if request method is POST
    if request.method == 'POST':
        user_input = request.form['city']

        # Check is user input is empty
        if not user_input:
            err_message = f"Error: no name entered"
            return render_template('index.html', error=err_message)
        
        try:
            # Fetch weather data for the given city using the API Key
            weather_data = fetch_weather(API_KEY, user_input)

            # Handle Errors that may occur
            if weather_data['cod'] == '404':
                err_message = f"API Error: {weather_data['message']}"
                return render_template('index.html', error=err_message)
            else:
                # If there are no errors, display the weather data
                weather_data = display_weather(weather_data)
                return render_template('index.html', data=weather_data)
        
        # Handle Exceptions that may occur
        except requests.exceptions.RequestException as net_err:
            err_message = f"Network Error: {net_err}"
            return render_template('index.html', error=err_message)
        except Exception as err:
            err_message = f"Error: {err}"
            return render_template('index.html', error=err_message)
        
    return render_template('index.html')

# Main function
if __name__ == "__main__":
    app.run(debug=True, port=8000)