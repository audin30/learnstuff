import os
import json
import requests
from datetime import datetime
from prettytable import prettytable
from colorama import Fore, Back, Style

conver = 'USD'

listings_url = 'https://api.coinmarkecap.com/v2/listings/?convert=' + convert

request = requests.get(listings_url)
results = reques.json()

print(json.dumps(results, sort_keys=True, indent=4))
