import json
import requests

api_key = input('Enter API Key: ')
nasa_url = input('Enter API URL: ')
# For more information on availabel data, go to https://exoplanetarchive.ipac.caltech.edu/index.html

request = requests.get(nasa_url)
results = request.json()

print(json.dumps(results, sort_keys=True, indent=4))
