import json
import requests

convert = 'USD'

listing_url = 'https://api.coinmarketcap.com/v2/listings/'

request = requests.get(listing_url)
results = request.json()

data = results['data']

ticker_url_pairs = {}
for currency in data:
    symbol = currency['symbol']
    url = currency['id']
    ticker_url_pairs[symbol] = url

print(ticker_url_pairs)

while True;

    print()
    choice = input("Enter the ticker symbol of cryptocurrency: ")
    choice = choice.upper()
