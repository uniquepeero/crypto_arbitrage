import requests
import json
import Exchange

# API URL https://api.hitbtc.com 
class HitBTC(Exchange):
	def __init__(self, url, public_key, secret):
        self.url = url + "/api/2"
        self.session = requests.session()
        self.session.auth = (public_key, secret)

	def get_ticker(self, symbol):
        return self.session.get('%s/public/ticker/%s' % (self.url, symbol)).json()

    def get_size(self, symbol):
    	session = requests.get('%s/public/orderbook/%s' % (self.url, symbol)).json()
    	data = {
    		'ask' : session['ask'][0],
    		'bid' : session['bid'][0]
    	}
    	return self.data

    def trading_commission(self, symbol):
    	session = requests.get('%s/trading/fee/%s' % (self.url, symbol)).json()

