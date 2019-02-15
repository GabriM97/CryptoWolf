"""
This class allows you to extract and save in JSON files all candlestick of a Market from a timestamp

"""

from Extractor import Extractor
from Time_Stamp_Converter import Time_Stamp_Converter as TSC
import json
import os

class JSON_Saver:
    
    # The save_on_file method starts the process to save the json file returned by API query
    def save_on_file(self, exchange, pair, date):
        d,m,y,h,mn = self.get_date_details(date)
        tsc_obj = TSC()
        timestamp = tsc_obj.convert(d,m,y,h,mn)
        self.save(exchange, pair, timestamp)


    # The save method allows to save the json file returned thanks to extract method. It will create directory if the filepath doesn't exists
    # (Part of save_on_file method)
    def save(self, exchange, pair, timestamp):
        candles = self.extract_candlestick(exchange, pair, timestamp)
        for period in candles.get("result"):
            filename = "{}.json".format(str(period))
            directory = "{}/{}/json/".format(exchange, pair)
            
            if not os.path.exists(directory):
                os.makedirs(directory)
            
            filepath = "{}{}".format(directory, filename)
            with open(filepath, "w") as out:
                json.dump({
                        "{}".format(period): candles["result"].get(period)
                },out)
    

    # The extract_candlestick method calls the function to extract OHLC data
    # (Part of save method)
    def extract_candlestick(self, exchange, pair, timestamp):
        extr = Extractor()
        print("\nQuerying the API ...")
        return extr.ohlc(exchange, pair, after=timestamp)


    # The make_date method return a dict with the date in input
    def make_date(self,day,month,year,hours,minutes):
        date = dict()
        date["day"] = day
        date["month"] = month
        date["year"] = year
        date["hours"] = hours
        date["mins"] = minutes
        return date


    # The get_date_details method returns single components of the date in input
    def get_date_details(self,date):
        day = int(date.get("day"))
        month = int(date.get("month"))
        year = int(date.get("year"))
        hours = int(date.get("hours"))
        mins = int(date.get("mins"))
        return day, month, year, hours, mins
