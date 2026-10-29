City Weather Reporter

Project Purpose

City Weather Reporter is a command-line python app that fetches

live current-weather data from OpenWeather. You enter the name of a city, and

It contents the city, country Code, temperature in Celsius which is currently posted by the program.

Humidity in percentage, and a short description of the weather

It also writes each successful outcome in city_data. csv and reads

the CSV to tell you (for each city how many records have been saved along with each)

city name and temperature.

Features

It validates user input and does not accept blank city name.

Gets live weather data using requests

Parses the API response using the json library.

– Deals with invalid cities, invalid api kits, network errors and malformed data.

City Data: Saves weather-related data skills. csv.

Utilises csv and with statements - safe file handling features.

Reads previously saved data for cities, gives names of the cities and temperatures.

X Gets the API key outside of the source code

Requirements

Python 3

requests library

A free OpenWeather API key

Using python — you can install this dependencies with the following command:

pip install -r requirements. txt

Getting an OpenWeather API Key

Step1 — Go to OpenWeather and create an account

Sign in to your account.

Go to API Keys section of your account

Create or copy an API key.

3- Do not keep the api key in your reporter. py.

Save the key into your OPENWEATHER_API_KEY environment variable.

Set the API Key

Windows PowerShell

$env:OPENWEATHER_API_KEY="YOUR_API_KEY_HERE"

python reporter.py

Windows Command Prompt

set OPENWEATHER_API_KEY=YOUR_API_KEY_HERE

python reporter.py

macOS or Linux

export OPENWEATHER_API_KEY="YOUR_API_KEY_HERE"

python3 reporter.py

You replace YOUR_API_KEY_HERE with your own OpenWeather API key.

How to Run the Program

Run:

python reporter.py

The program will prompt:

Enter a city name:

Example:

Enter a city name: Dubai

Current Weather

City: Dubai

Country: AE

Temperature: 30.2 °C

Humidity: 55%

Description: Clear Sky

Weather data saved to city_data. csv.

City found in the file: 1

Dubai: 30.2 °C

The weather values as seen above is just a sample. The actual values come

from the live API during program execution.

CSV Output

The program creates city_data. csv with these columns:

City

Country

Temperature (C)

Humidity (%)

Description

After each proper run of this program each record from the city increases.

Project Files

reporter. py - main Python program

requirements. txt - required Python package

-. gitignore - don't commit generated files (or sensitive files)

city_data. csv - This file is created automatically when your program runs successfully.

Security

