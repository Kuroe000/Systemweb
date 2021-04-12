import requests
import json

print('Temperature of São Paulo')
req = None
city='455827'
link = 'https://api.hgbrasil.com/weather?woeid='+city
try:
    print(f'Searching for: {link}')
    req = requests.get(link)
    if(req.status_code == 200):
        print("Success")
    result = dict(json.loads(req.text))
    result = result['results']
    forecast = result['forecast']
    max = forecast[0]['max']
    min = forecast[0]['min']
    temp = result['temp']
    print(f'Temperature {temp}C Max {max}C Min {min}C')
except Exception as error:
    print(f'Couldnt possible to obtain the weather date for the token {city}: {error}')
    print(req)
