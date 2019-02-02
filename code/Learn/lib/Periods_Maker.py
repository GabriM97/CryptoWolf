'''
This class is a Facility for ohlc method of Extractor Class. 
This class helps you to make right "periods" paramiter for ohlc method of Extractor Class

'''

class Periods_Maker:

	#The costructor inizializes a dictionary containing the correct candles types.
	def __init__ (self):
		self.diz={"1-m":"60", "3-m":"180", "5-m":"300", "15-m":"900", "30-m":"1800", "1-h":"3600", "2-h":"7200", "4-h":"14400", "6-h":"21600", "12-h":"43200", "1-d":"86400", "3-d":"259200", "1-w":"604800"}
		self.rev_diz={"60":"1-m", "180":"3-m", "300":"5-m", "900":"15-m", "1800":"30-m", "3600":"1-h", "7200":"2-h", "14400":"4-h", "21600":"6-h", "43200":"12-h", "86400":"1-d", "259200":"3-d", "604800":"1-w"}

	#The make method creates a correct "periods" paramiter if you pass the correct candles types, otherwise method returns an error code that represents a "Bad Request" Message
	def make (self,list_periods):
		if (len(list_periods)==0): return -1
		st="'1,"
		for i in range (len(list_periods)):
			if (list_periods[i] not in self.diz.values()):
				return -1
			st+=list_periods[i]
			st+=","
		st+="1'"
		return st

	#The print_candles_types method prints all candles types avaible
	def print_candles_types (self):
		print (self.diz)

	#The ret_diz method returns the list of candles types avaible
	def ret_diz (self):
		return self.diz

	#The ret_rev_diz method returns the reverse-list of candles types avaible
	def ret_rev_diz (self):
		return self.rev_diz
			
