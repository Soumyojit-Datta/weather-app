# Weather App

An open-source Python weather app that fetches and displays real-time weather data using the **OpenWeatherAPI**.

## Features

- Fetches current weather data for any location.
- Displays a 5-day weather forecast with optional user input.

## Prerequisites

- **Python**: Ensure Python is installed. The app also requires the `requests` library.
- **OpenWeatherAPI Key**: You'll need an API key from [OpenWeather](https://openweathermap.org/api) to use the app.

## Installation

1. **Clone the repository**

   Download the app by cloning this repository:

   ```bash
   git clone <repository-url>
   ```
2.  **Install Dependencies**

    Navigate to the project directory and install the required dependencies:

    For Windows:
   
    ```bash
    py -m pip install requests
    ```
	
    For Linux/macOS:
	
    ```bash
    pip3 install requests
    ```
	

Make sure that your **OpenWeatherAPI key** is present inside of `config.json` in the `api_key` entry instead of `your_api_key_here`

## Usage

1. **Check current weather:**
	
	On Windows:
	
	```bash
	py main.py <location>
	```
	
	On Linux/macOS:
	
	```bash
	python3 main.py <location>
	```
	Replace `location` with the name of your city (e.g., `London`)
	
2. **Display the temperature in Fahrenheit (°F):**

	By default, the temperature is shown in Celsius (°C). To display it in Fahrenheit, use the `-u f` flag:
	
	On Windows:
	
	```bash
	py main.py <location> -u f
	```
	
	On Linux/macOS:
	
	```bash
	python3 main.py <location> -u f
	```

3.  **Get a 5-day weather forecast:**
	
	To see a 5-day forecast for a location, use the `-f` flag:
	
	On Windows:
	
	```bash
	py main.py <location> -f
	```
	
	On Linux/macOS:
	
	```bash
	python3 main.py <location> -f
	```
	
	Replace <location> with your desired city name.
