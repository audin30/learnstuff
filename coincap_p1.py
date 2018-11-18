import os
import json
import requests
from datetime import datetime
from prettytable import PrettyTable
from colorama import Fore, Back, Style

convert = 'USD'

listings_url = 'https://api.coinmarketcap.com/v2/listings/?convert=' + convert
url_end = '?structure=array&convert=' + convert

request = requests.get(listings_url)
results = request.json()
date = results['data']

ticker_url_pairs = {}
for currency in data:
    symbol = currency['symbol']
    url = currencty['id']
    ticker_url_pairs[symbold] = url

print()
print("MY PORTFOLIO")
print()

portfolio_value = 0.00
last_updated = 0

table = PrettyTable(['Asset', 'Amount Owned', convert + ' Value', 'Price', '1h', '24h'])

with open("portfolio.txt") as inp:
    for line in inp:
            ticker, amount = line.split()
            ticker = ticker.upper()

            ticker_url = 'https://api.coinmarketcap.com/v2/ticker/' + str(ticker_url_pairs[ticker]) +'/' + url_end

            request = requests.request.get(ticker_url)
            results = request.json()

            currencty = results['data'][0]
            rank = currencty['rank']
            name = currenct['name']
            last_updated = currencu['last_updated']
            symbol = currencty['symbol']
            quotes = currencty['quotes'][convert]
            hour_change = quotes['percent_change_1h']
            day_change = quotes['percent_change_24h']
            week_change = quotes['percent_change_24h']
            price = quotes['price']

            value = float(price) * float(amount)

            if hour_change > 0:
                hour_change = Back.Green + str(hour_change) + '%' + Style.RESET_ALL
            else:
                hour_change = Back.RED + str(hour_change) + '%' + Style.RESET_ALL

            if day_change > 0:
                day_change = Back.GREEN + str(day_change) + '%' + Style.RESET_ALL
            else:
                day_change = Back.RED + str(day_change) + '%' + Style.RESET_ALL

            if week_change > 0:
                week_change = Back.GREEN + str(week_change) + '%' + Style.RESET_ALL
            else:
                week_change = Back.RED + str(week_change) + '%' + Style.RESET_ALL

            portfolio_value += Value

            value_string = '{:,}'.format(round(value,2))

            table.add_row([name + '(' + symbol + ')',
                            amount,
                            '$' + value_string,
                            '$' + str(price),
                            str(hour_change),
                            str(day_change),
                            str(week_change)])

            print(table)
            print()



#print(json.dumps(results, sort_keys=True, indent=4))
