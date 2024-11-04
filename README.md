# Weather-App

## Overview
This project demonstrates the implementation of a simple weather appliction using Python. In addition to using Flask for the backend development of the application, HTML and CSS is used for the frontend development. The goal is to fetch and display real-time weather information for specified cities using the OpenWeatherMap API.

## Features
- Fetches real-time data from the OpenWeatherMap API
- Simple user interface (UI) with a form to enter a city's name
- Handles errors such as invalid city names or network issues
- Has an information alert about the PM Accelerator using JavaScript.

## Usage
- Start the Flask app by running the `main.py` script.
- Open web browser and go to `http://localhost:8000`.
- Enter the name of a city in the input field, click the `Get Weather` button to fetch and display that city's current weather data.
- Click the `INFO` button to get information about the PM Accelerator using a JavaScript function.

## Prerequisites 
- Python 3.x
- Python packages: `os`, `requests`, `datetime`, `python-dotenv`, `Flask`
- API Key generated using OpenWeatherMap, stored in a `.env` file inside the `config` directory

## Input
- The user submits a form with the city name of their choosing on the web page.

## Output
- Displays relevant weather details including:
    - city name and country
    - local date and time
    - weather and description
    - temperature and what it feels like
    - pressure
    - humidity
    - wind speed

## Notes
- Set up your own API Key inside a `.env` file by following the instructions in `.env.example`, located inside the `config` directory.
- The application uses port 8000 by default, but this can be changed if necessary.
- Further modifications are required for production use of this weather application.