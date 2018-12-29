from Extractor import Extractor as a 
from Time_Stamp_Converter import Time_Stamp_Converter as tp

#TEST CLASS TIME_STAMP_CONVERTER
obj=tp()
val=obj.convert (1,11,2017,5,23)
print (val)
obj.print_last_timestamp()

#TEST CLASS EXTRACTOR - OHLC METHOD
b=a()
x=b.ohlc ("coinbase-pro","btcusd","1262300400",-5,-5)
print (x['result'])



