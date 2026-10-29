import csv
import json
import os

import requests


API_URL = "https://api.openweathermap.org/data/2.5/weather"
CSV_FILE = "city_data.csv"
FIELDNAMES = [
    "City",
    "Country",
    "Temperature (C)",
    "Humidity (%)",
    "Description",
]


def get_city_name():
    """Prompt the user until a non-empty city name is entered."""
    while True:
        city = input("Enter a city name: ").strip()
        if city:
            return city

        print("City name cannot be empty. Please try again.")


def get_weather_data(city, api_key):
    """Retrieve and parse current weather data for a city."""
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
    }

    try:
        response = requests.get(API_URL, params=params, timeout=10)
    except requests.RequestException as error:
        print(f"Network error: {error}")
        return None

    if response.status_code == 404:
        print(f'City "{city}" was not found.')
        return None

    if response.status_code == 401:
        print("API key error. Check that your OpenWeather API key is valid.")
        return None

    if response.status_code != 200:
        print(f"API error: HTTP {response.status_code}")
        return None

    try:
        data = json.loads(response.text)

        return {
            "City": data["name"],
            "Country": data["sys"]["country"],
            "Temperature (C)": round(data["main"]["temp"], 1),
            "Humidity (%)": data["main"]["humidity"],
            "Description": data["weather"][0]["description"].title(),
        }
    except (json.JSONDecodeError, KeyError, IndexError, TypeError) as error:
        print(f"Could not process the weather data: {error}")
        return None


def display_weather(weather):
    """Print a formatted weather summary to the console."""
    print("\nCurrent Weather")
    print("---------------------------")
    print(f"City: {weather['City']}")
    print(f"Country: {weather['Country']}")
    print(f"Temperature: {weather['Temperature (C)']} °C")
    print(f"Humidity: {weather['Humidity (%)']}%")
    print(f"Description: {weather['Description']}")


def write_weather_to_csv(weather):
    """Append weather data to the CSV file and add headers if needed."""
    file_has_data = (
        os.path.exists(CSV_FILE)
        and os.path.getsize(CSV_FILE) > 0
    )

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)

        if not file_has_data:
            writer.writeheader()

        writer.writerow(weather)

    print(f"\nWeather data saved to {CSV_FILE}.")


def report_saved_cities():
    """Read the CSV file and report saved city names and temperatures."""
    try:
        with open(
            CSV_FILE,
            "r",
            newline="",
            encoding="utf-8",
        ) as csv_file:
            reader = csv.DictReader(csv_file)
            rows = list(reader)
    except FileNotFoundError:
        print("\nNo saved city data was found.")
        return

    print(f"\nCities currently in the file: {len(rows)}")

    if not rows:
        print("No city records are available.")
        return

    for row in rows:
        print(f"- {row['City']}: {row['Temperature (C)']} °C")


def main():
    """Run the command-line city weather reporter."""
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        print("OPENWEATHER_API_KEY is not set.")
        print("Set the environment variable, then run the program again.")
        return

    city = get_city_name()
    weather = get_weather_data(city, api_key)

    if weather is None:
        return

    display_weather(weather)
    write_weather_to_csv(weather)
    report_saved_cities()


if __name__ == "__main__":
    main()

