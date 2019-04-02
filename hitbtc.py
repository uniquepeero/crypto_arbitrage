import requests
import json

class HitBTC:
    def get_ticker_symbol(self, symbol):
        url = 'https://api.hitbtc.com/api/2/public/ticker' + symbol
        response = requests.get(url)
        return response


hitbtc = HitBTC()
print(hitbtc.get_ticker_symbol('ETHBTC'))
