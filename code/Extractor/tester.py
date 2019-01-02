from Extractor import Extractor
from Time_Stamp_Converter import Time_Stamp_Converter
from Periods_Maker import Periods_Maker
import numpy as np

#TEST CLASS TIME_STAMP_CONVERTER
obj=Time_Stamp_Converter()

after=obj.convert (1,7,2005,16,0) 
print (after) #EXPECTED: 1120226400

print("")

date_time=obj.get_date (1120226400) 
print (date_time) #EXPECTED: 01-07-2005 16:00

print("")

#TEST CLASS PERIODS_MAKER
b=Periods_Maker()

dic=b.ret_diz()
dic_rev=b.ret_rev_diz()

b.print_candles_types()
list_of_types_candles=[dic['1-m'],dic['3-m']]
periods=b.make (list_of_types_candles)

if (periods==-1): 
	print ("Error, you have inserted an/some Unknown Candle/es Type/es \n")
	exit()

print("\n")

#TEST CLASS EXTRACTOR - OHLC METHOD
b=Extractor()

x=b.ohlc ("coinbase-pro","btcusd",-5,after,periods)

if (type(x)==int and x==-1): 
	print ("Bad Request \n") 

elif (type(x)==int and x==-2):
	print ("You have finished your CPU allowance, retry next hour \n")

elif (type(x)==int and x==-3):
	print ("Unexpected Error, retry please \n")

else:
	candles_types_returned=list(x['result'].keys())
	print ("Candles Types Returned: ({}, {}) ".format(dic_rev[candles_types_returned[1]],dic_rev[candles_types_returned[0]]))

	candle_1_minute=x['result'][dic['1-m']]
	candle_3_minutes=x['result'][dic['3-m']]

	print ("Size 1-Minute Candle: ({}, {})".format(len(candle_1_minute),len(candle_1_minute[0])))
	print ("Size 3-Minutes Candle: ({}, {})".format(len(candle_3_minutes),len(candle_3_minutes[0])))

	print ("Example 1-Minute Candle: {} ".format(candle_1_minute[0]))
	print ("Example 3-Minutes Candle: {} ".format(candle_3_minutes[0]))

