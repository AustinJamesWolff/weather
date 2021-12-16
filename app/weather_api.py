import requests

response = requests.get('https://www.metaweather.com/api/location/44418/')

response = response.json()

print(response)