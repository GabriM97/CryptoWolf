from Extractor import Extractor as a 
from Time_Stamp_Converter import Time_Stamp_Converter as tp

#TEST CLASS TIME_STAMP_CONVERTER
obj=tp()
val=obj.convert (4,9,2014,14,0)
print (val)
print (type(val))
obj.print_last_timestamp()

#TEST CLASS EXTRACTOR - OHLC METHOD
b=a()
x=b.ohlc ("coinbase-pro","btcusd",val,-5,-5)
print (x['result'])



