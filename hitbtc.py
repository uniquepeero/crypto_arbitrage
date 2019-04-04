import requests
import json


# API URL https://api.hitbtc.com
class HitBTC:
	def __init__(self, url, public_key, secret):
		self.url = url + "/api/2"
		self.session = requests.session()
		self.session.auth = (public_key, secret)

	def get_ticker(self, symbol):
		return self.session.get(f'{self.url}/public/ticker/{symbol}').json()

	def get_size(self, symbol):
		session = requests.get(f'{self.url}/public/orderbook/{symbol}').json()
		data = {
			'ask': session['ask'][0],
			'bid': session['bid'][0]
		}
		return data

	def trading_commission(self, symbol):
		return self.session.get('%s/trading/fee/%s' % (self.url, symbol)).json()

hitbtc = HitBTC('https://api.hitbtc.com', 'a8380f7a8e941f0ca70ba26af25dbb34', '6951fc4e522157c67cee5fbc00ad86e6')
symbol = 'ETHBTC'
print(f"{symbol} ask: {hitbtc.get_size(symbol)['ask']} \
		\n{symbol} bid: {hitbtc.get_size(symbol)['bid']}")
print(hitbtc.trading_commission(symbol))
