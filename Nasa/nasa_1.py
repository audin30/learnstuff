import json
import requests

api_key = input('Enter API Key: ')
nasa_url = input('Enter API URL: ')
#nasa_url = 'https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&format=json'

request = requests.get(nasa_url)
results = request.json()

print(json.dumps(results, sort_keys=True, indent=4))
