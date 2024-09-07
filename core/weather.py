import requests
import json

class WeatherClient:
    def __init__(self, config_file):
        with open(config_file, 'r') as f:
            self.config = json.load(f)
        self.api_key = self.config['api_key']
        self.base_url = self.config['base_url']

    def get_weather(self, location):
        url = f"{self.base_url}weather?q={location}&appid={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code}")

    def get_forecast(self, location):
        url = f"{self.base_url}forecast?q={location}&appid={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code}")

    def get_uv_index(self, lat, lon):
        url = f"{self.base_url}uvi?lat={lat}&lon={lon}&appid={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['value']
        else:
            raise Exception(f"Error: {response.status_code}")

    def get_air_quality(self, lat, lon):
        """Fetch air quality index (AQI) for the specified latitude and longitude."""
        url = f"{self.base_url}air_pollution?lat={lat}&lon={lon}&appid={self.api_key}"
        response = requests.get(url)
        return response.json()

    def display_aqi(self, aqi):
        """Interpret and display the AQI level."""
        aqi_levels = {
            1: "Good",
            2: "Fair",
            3: "Moderate",
            4: "Poor",
            5: "Very Poor"
        }
        return aqi_levels.get(aqi, "Unknown")
