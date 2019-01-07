from Extractor import Extractor as EXTR 
from Time_Stamp_Converter import Time_Stamp_Converter as TSC
from JSON_Saver import JSON_Saver as JSave
from Dataset_Maker import Dataset_Maker as DataMak
from Periods_Maker import Periods_Maker as PM
from Dataset_Creator import Dataset_Creator as DC

def test_tm_stmp_cnvrt():
    #TEST CLASS TIME_STAMP_CONVERTER
    obj=TSC()
    val=obj.convert (1,7,2005,16,0)
    print (val) #EXPECTED: 1120226400
    date_time=obj.get_date (1120226400)
    print (date_time) #EXPECTED: 01-07-2005 16:00
    print("\n")


def test_Period_Maker():
    #TEST CLASS PERIODS_MAKER
    obj=PM()
    dic=obj.ret_diz()
    dic_rev=obj.ret_rev_diz()
    obj.print_candles_types()
    
    list_of_types_candles=[dic['1-m'], dic['3-m']]
    print(list_of_types_candles) #EXPECTED ['60','180']
    periods=obj.make(list_of_types_candles)
    
    if (periods==-1): 
    	print ("Error, you have inserted an/some Unknown Candle/es Type/es \n")
    	exit()
    print("\n")
    return periods, dic, dic_rev

def test_Extractor():
    #TEST CLASS EXTRACTOR - OHLC METHOD
    obj=TSC()   
    val=obj.convert(4,9,2014,1,0)

    obj=PM()
    dic=obj.ret_diz()
    dic_rev=obj.ret_rev_diz()
    list_of_types_candles=[dic['1-m'], dic['3-m']]
    per=obj.make(list_of_types_candles)
    
    ext=EXTR()
    x=ext.ohlc ("coinbase-pro","btcusd",after=val,periods=per)
    
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
    
# Saver for each candlestick
def test_JSON_Saver():
    #TEST CLASS JSON_SAVER - SAVE_ON_FILE METHOD
    jsav = JSave()
    date = jsav.make_date(1,1,2011,0,0)
    exchange = "bitstamp"
    pair = "btcusd"
    
    jsav.save_on_file(exchange, pair, date)
    print("Candles Stick Saved!")
    
# Create a dataset for only one period of candlestick
def test_Dataset_Maker():
    #TEST CLASS DATASET_MAKER - LOAD_JSON AND PRINT_CONTAINER
    exchange = "bitstamp"
    pair = "btcusd"
    per_mak = PM()
    periods_list = per_mak.ret_diz()
    period = periods_list["12-h"]
    
    dataMaker = DataMak(exchange, pair)
    dataset = dataMaker.load_json_candlestick(period)
    dataMaker.print_datas(dataset)
    dataMaker.save_on_file(dataset)

# "Automatic" process to create a Dataset
def test_Dataset_Creator():
    #TEST CLASS DATASET_CREATOR - RUN_ALL AND RUN_ONLY_MAKER
    exchange = "bitstamp"
    pair = "btcusd"
    period = "12-h"  # Has to respect the Periods_Maker class style

    obj = DC(exchange, pair)
    
    # At the first run you have to call run_all method to download JSON files
    dataset = obj.run_all(period)
    #dataset = obj.run_only_maker(period)
        
    
#  ------  MAIN  ------

#test_tm_stmp_cnvrt()
#test_Period_Maker()
#test_Extractor()
#test_JSON_Saver()
#test_Dataset_Maker()
test_Dataset_Creator()