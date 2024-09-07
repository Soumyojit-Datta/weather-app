# utils.py

from datetime import datetime, timedelta, timezone

def get_wind_direction(degrees):
    directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    idx = int((degrees + 11.25) / 22.5) % 16
    return directions[idx]

def convert_temperature(temp_kelvin, unit):
    if unit == 'c':
        return temp_kelvin - 273.15  # Convert to Celsius
    elif unit == 'f':
        return (temp_kelvin - 273.15) * 9/5 + 32  # Convert to Fahrenheit
    return temp_kelvin

def format_time(timestamp, tz_offset):
    """Convert a Unix timestamp to local time based on the timezone offset."""
    utc_time = datetime.fromtimestamp(timestamp, tz=timezone.utc)  # Convert to UTC
    local_time = utc_time + timedelta(seconds=tz_offset)  # Adjust by the timezone offset
    return local_time.strftime('%Y-%m-%d %H:%M:%S')  # Format the date and time