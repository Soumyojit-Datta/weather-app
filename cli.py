import argparse
from core.weather import WeatherClient
from core.utils import convert_temperature, get_wind_direction, format_time

def parse_args():
    parser = argparse.ArgumentParser(description='CLI Weather App')
    parser.add_argument('location', type=str, help='Location for weather information')
    parser.add_argument('-f', '--forecast', action='store_true', help='Get 5-day forecast')
    parser.add_argument('-u', '--unit', choices=['c', 'f'], default='c', help='Temperature unit: c for Celsius, f for Fahrenheit')
    return parser.parse_args()

def main():
    args = parse_args()
    weather_client = WeatherClient('config/config.json')

    if args.forecast:
        forecast_data = weather_client.get_forecast(args.location)
        print(f"5-day forecast for {args.location}:")
        for forecast in forecast_data['list']:
            dt = format_time(forecast['dt'], forecast_data['city']['timezone'])
            temp = convert_temperature(forecast['main']['temp'], args.unit)
            description = forecast['weather'][0]['description']
            print(f"{dt}: {temp:.2f}°{'F' if args.unit == 'f' else 'C'}, {description}")
    else:
        data = weather_client.get_weather(args.location)
        lat = data['coord']['lat']
        lon = data['coord']['lon']
        aqi_data = weather_client.get_air_quality(lat, lon)
        aqi = aqi_data['list'][0]['main']['aqi']
        aqi_description = weather_client.display_aqi(aqi)
        temp = convert_temperature(data['main']['temp'], args.unit)
        feels_like = convert_temperature(data['main']['feels_like'], args.unit)
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        wind_deg = data['wind']['deg']
        pressure = data['main']['pressure']
        wind_direction = get_wind_direction(wind_deg)
        visibility = data['visibility'] / 1000
        description = data['weather'][0]['description']
        uv_index = weather_client.get_uv_index(lat, lon)
        sunrise = format_time(data['sys']['sunrise'], data['timezone'])
        sunset = format_time(data['sys']['sunset'], data['timezone'])

        print(f"Current weather in {args.location}:")
        print(f"Temperature: {temp:.2f}°{'F' if args.unit == 'f' else 'C'} (Feels like: {feels_like:.2f}°{'F' if args.unit == 'f' else 'C'})")
        print(f"Weather: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s, Direction: {wind_direction}")
        print(f"Visibility: {visibility:.2f} km")
        print(f"Pressure: {pressure} hPa")
        print(f"Sunrise: {sunrise}")
        print(f"Sunset: {sunset}")
        print(f"UV Index: {uv_index}")
        print(f"Air Quality: {aqi} ({aqi_description})")

