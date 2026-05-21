import requests
api_key = "ecb2831b687445fbb92c97c8e07cbcc7"
api_url = f"https://api.weatherstack.com/current?access_key={api_key}&query=New York"

# def fetch_data():
#     print("Fetching weather data from Weatherstack API...")
#     try:
#         response = requests.get(api_url)
#         response.raise_for_status()
#         print("API response received successfully.")
#         return response.json()

#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred:{e}")
#         raise

# fetch_data()

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2026-05-21 00:42', 'localtime_epoch': 1779324120, 'utc_offset': '-4.0'}, 'current': {'observation_time': '04:42 AM', 'temperature': 19, 'weather_code': 116, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png'], 'weather_descriptions': ['Partly Cloudy '], 'astro': {'sunrise': '05:34 AM', 'sunset': '08:12 PM', 'moonrise': '10:22 AM', 'moonset': '12:40 AM', 'moon_phase': 'Waxing Crescent', 'moon_illumination': 24}, 'air_quality': {'co': '140.85', 'no2': '8.65', 'o3': '54', 'so2': '1.65', 'pm2_5': '3.45', 'pm10': '3.55', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 19, 'wind_degree': 340, 'wind_dir': 'NNW', 'pressure': 1019, 'precip': 0, 'humidity': 36, 'cloudcover': 55, 'feelslike': 19, 'uv_index': 0, 'visibility': 10, 'is_day': 'no'}}