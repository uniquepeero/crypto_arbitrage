import requests
import json
import configparser


# API URL https://api.hitbtc.com
class HitBTC:
	def __init__(self):
		self.url = "https://api.hitbtc.com/api/2"
		self.public_key = ""
		self.secret = ""
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
		return self.session.get(f'{self.url}/trading/fee/{symbol}').json()

	def read_config(self, cfg_file):
		#if not os.path.isfile(cfg_file):
			# TODO Вставить сюда логирование ошибки "Файл не найден"
			#self.log("Missing config file")
		# TODO Сделать через try:
		config = configparser.RawConfigParser()
		config.read(cfg_file)
		self.public_key = config.get('HitBTC', 'public_key')
		self.secret = config.get('HitBTC', 'secret')


if __name__ == '__main__':
	hitbtc = HitBTC()
	
	symbol = 'ETHBTC'
	print(f"{symbol} ask: {hitbtc.get_size(symbol)['ask']} \
			\n{symbol} bid: {hitbtc.get_size(symbol)['bid']}")
	print(hitbtc.trading_commission(symbol))