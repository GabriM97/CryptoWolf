"""

This class allows you to retrieve data from the CryptoWatch's REST API
 
"""

import urllib.request, json

class Extractor:

	#The retrieve_data method allows you to forward a request to the server
	def retrieve_data (self,index):
		try:
			with urllib.request.urlopen(index) as url:
				data=json.loads(url.read().decode())
			return data	
		except urllib.error.HTTPError as e:
			if (e.code==400):
				return -1
			if (e.code==429):
				return -2	
		except:
			return -3

	#The asset_index method allows you to retrieve the list of all coins
	def asset_index (self):
		return self.retrieve_data ("https://api.cryptowat.ch/assets")

	#The asset_details method allows you to retrieve the list of all markets which have a specific coin as a base or quote
	def asset_details (self,coin):
		index="https://api.cryptowat.ch/assets/"
		index+=coin
		return self.retrieve_data (index)

	#The pair_index method allows you to retrieve the list of all pairs avaible
	def pair_index (self):
		return self.retrieve_data("https://api.cryptowat.ch/pairs")

	#The pair_details method allows you to retrieve the list of all markets for a specific pair
	def pair_details (self,pair):
		index="https://api.cryptowat.ch/pairs/"
		index+=pair
		return self.retrieve_data (index)

	#The exchange_index method allows you to retrieve the list of all exchanges avaible
	def exchange_index (self):
		return self.retrieve_data("https://api.cryptowat.ch/exchanges")

	#The exchange_details method allows you to retrieve some information about a specific exchange
	def exchange_details (self,exchange):
		index="https://api.cryptowat.ch/exchanges/"
		index+=exchange
		return self.retrieve_data (index)

	#The market_index method allows you to retrieve the list of all markets avaible
	def market_index (self):	
		return self.retrieve_data("https://api.cryptowat.ch/markets")

	#The market_index_exchange method allows you to retrieve the list of all markets avaible in a specific exchange
	def market_index_exchange (self,exchange): 
		index="https://api.cryptowat.ch/markets/"
		index+=exchange
		return self.retrieve_data (index)

	#The market_details method allows you to retrieve some informations about a specific market
	def market_details (self,exchange,pair):
		index="https://api.cryptowat.ch/markets/"
		index+=exchange
		index+="/"
		index+=pair
		return self.retrieve_data (index)

	#The market_price method allows you to retrieve the lastest price of a specific market
	def market_price (self,exchange,pair):
		index="https://api.cryptowat.ch/markets/"
		index+=exchange
		index+="/"
		index+=pair
		index+="/"
		index+="price"
		return self.retrieve_data (index)	

	#The market_summary method returns a market's last price as well as other stats based on a 24-hour sliding window.
	def market_summary (self,exchange,pair):
		index="https://api.cryptowat.ch/markets/"
		index+=exchange
		index+="/"
		index+=pair
		index+="/"
		index+="summary"
		return self.retrieve_data (index)	

	#The market_trades method returns a market's most recent trades, incrementing chronologically.
	def market_trades (self,exchange,pair,limit=-5,since=-5):
		if (limit==-5 and since==-5):
			index="https://api.cryptowat.ch/markets/"
			index+=exchange
			index+="/"
			index+=pair
			index+="/"
			index+="trades"
			return self.retrieve_data (index)
		elif (limit!=-5 and since==-5):
			index="https://api.cryptowat.ch/markets/"
			index+=exchange
			index+="/"
			index+=pair
			index+="/"
			index+="trades"
			index+="?limit="
			index+=limit
			return self.retrieve_data (index)
		elif (since!=-5 and limit==-5):
			index="https://api.cryptowat.ch/markets/"
			index+=exchange
			index+="/"
			index+=pair
			index+="/"
			index+="trades"
			index+="?since="
			index+=since
			return self.retrieve_data (index)
		elif (limit!=-5 and since!=-5):
			index="https://api.cryptowat.ch/markets/"
			index+=exchange
			index+="/"
			index+=pair
			index+="/"
			index+="trades"
			index+="?limit="
			index+=limit
			index+="&since="
			index+=since
			return self.retrieve_data (index)	

	#The market_order_book method returns a market's order book
	def market_order_book (self,exchange,pair,limit=-5,depht=-5,span=-5):
		if (limit==-5 and depht==-5 and span==-5):
			index="https://api.cryptowat.ch/markets/"
			index+=exchange
			index+="/"
			index+=pair
			index+="/"
			index+="orderbook"
		elif (limit!=-5 and depht==-5 and span==-5):
			index="https://api.cryptowat.ch/markets/"
			index+=exchange
			index+="/"
			index+=pair
			index+="/"
			index+="orderbook"
			index+="?limit="
			index+=limit	
			return self.retrieve_data (index)
		elif (depht!=-5 and limit==-5 and span==-5):
			index="https://api.cryptowat.ch/markets/"
			index+=exchange
			index+="/"
			index+=pair
			index+="/"
			index+="orderbook"
			index+="?depht="
			index+=depht	
			return self.retrieve_data (index) 
		elif (span!=-5 and limit==-5 and depht==-5):
			index="https://api.cryptowat.ch/markets/"
			index+=exchange
			index+="/"
			index+=pair
			index+="/"
			index+="orderbook"
			index+="?span="
			index+=span	
			return self.retrieve_data (index)
		elif (depht!=-5 and limit!=-5 and span==-5):
			index="https://api.cryptowat.ch/markets/"
			index+=exchange
			index+="/"
			index+=pair
			index+="/"
			index+="orderbook"
			index+="?depht="
			index+=depht	
			index+="&limit="
			index+=limit
			return self.retrieve_data (index)
		elif (depht!=-5 and limit==-5 and span!=-5):
			index="https://api.cryptowat.ch/markets/"
			index+=exchange
			index+="/"
			index+=pair
			index+="/"
			index+="orderbook"
			index+="?depht="
			index+=depht	
			index+="&span="
			index+=span
			return self.retrieve_data (index)
		elif (depht==-5 and limit!=-5 and span!=-5):
			index="https://api.cryptowat.ch/markets/"
			index+=exchange
			index+="/"
			index+=pair
			index+="/"
			index+="orderbook"
			index+="?span="
			index+=span	
			index+="&limit="
			index+=limit
			return self.retrieve_data (index)
		elif (depht!=-5 and limit!=-5 and span!=-5):
			index="https://api.cryptowat.ch/markets/"
			index+=exchange
			index+="/"
			index+=pair
			index+="/"
			index+="orderbook"
			index+="?depht="
			index+=depht	
			index+="&limit="
			index+=limit
			index+="&span="
			index+=span
			return self.retrieve_data (index)

	#The ohlc method returns a market's OHLC candlestick data.
	def ohlc (self,exchange,pair,before=-5,after=-5,periods=-5):
		if (before==-5 and after==-5 and periods==-5):
			index="https://api.cryptowat.ch/markets/"
			index+=exchange
			index+="/"
			index+=pair
			index+="/"
			index+="ohlc"
			return self.retrieve_data (index)
		elif (before!=-5 and after==-5 and periods==-5):
			index="https://api.cryptowat.ch/markets/"
			index+=exchange
			index+="/"
			index+=pair
			index+="/"
			index+="ohlc"
			index+="?before="
			index+=before
			return self.retrieve_data (index)	
		elif (after!=-5 and before==-5 and periods==-5):
			index="https://api.cryptowat.ch/markets/"
			index+=exchange
			index+="/"
			index+=pair
			index+="/"
			index+="ohlc"
			index+="?after="
			index+=after
			return self.retrieve_data (index)
		elif (before!=-5 and after!=-5 and periods==-5):
			index="https://api.cryptowat.ch/markets/"
			index+=exchange
			index+="/"
			index+=pair
			index+="/"
			index+="ohlc"
			index+="?before="
			index+=before
			index+="&after="
			index+=after
			return self.retrieve_data (index)
		elif (periods!=-5 and before==-5 and after==-5):
			index="https://api.cryptowat.ch/markets/"
			index+=exchange
			index+="/"
			index+=pair
			index+="/"
			index+="ohlc"
			index+="?periods="
			index+=periods
			return self.retrieve_data (index)
		elif (periods!=-5 and before!=-5 and after==-5):
			index="https://api.cryptowat.ch/markets/"
			index+=exchange
			index+="/"
			index+=pair
			index+="/"
			index+="ohlc"
			index+="?periods="
			index+=periods
			index+="&before="
			index+=before
			return self.retrieve_data (index)	
		elif (periods!=-5 and after!=-5 and before==-5):
			index="https://api.cryptowat.ch/markets/"
			index+=exchange
			index+="/"
			index+=pair
			index+="/"
			index+="ohlc"
			index+="?periods="
			index+=periods
			index+="&after="
			index+=after
			return self.retrieve_data (index)
		elif (periods!=-5 and before!=-5 and after!=-5):
			index="https://api.cryptowat.ch/markets/"
			index+=exchange
			index+="/"
			index+=pair
			index+="/"
			index+="ohlc"
			index+="?periods="
			index+=periods
			index+="&before="
			index+=before
			index+="&after="
			index+=after
			return self.retrieve_data (index)
			

	#The prices method returns the current price for all supported markets.
	def prices (self):
		return self.retrieve_data("https://api.cryptowat.ch/markets/prices")

	#The summaries method returns the market summary for all supported markets.
	def summaries (self):
		return self.retrieve_data("https://api.cryptowat.ch/markets/summaries")	