"""
This class helps to create the Dataset.
An instance of this class is unique for the exchange and the pair.
With this object it's possible generate datasets for each passed period via parameter

"""

from JSON_Saver import JSON_Saver as JSave
from Dataset_Maker import Dataset_Maker as DM
from Periods_Maker import Periods_Maker as PM


class Dataset_Creator:
    
    def __init__(self, exchange, pair):        
        self.exchange = exchange
        self.pair = pair
        
        self.jsav = JSave()
        self.periodMaker = PM()
        self.dataMaker = DM(exchange, pair)

        
    # The run_all method allows to have the most recently json files and than create the dataset for the period in input
    def run_all(self, period):
        periods_list = self.periodMaker.ret_diz()
        self.period = periods_list[period]
        
        self.save_json()
        dataset = self.make_dataset(self.period)
        self.dataMaker.print_data(dataset)
        return dataset
    
    
    # The run_only_maker method allows to create the dataset, for the period in input, based on the last json files downloaded
    def run_only_maker(self, period):
        periods_list = self.periodMaker.ret_diz()
        self.period = periods_list[period]
        
        dataset = self.make_dataset(self.period)
        self.dataMaker.print_data(dataset)
        return dataset   
    
    
    # The save_json method downloads and saves the json files
    def save_json(self):
        date = self.jsav.make_date(1,1,2011,0,0)
        self.jsav.save_on_file(self.exchange, self.pair, date)
        print("Candles Stick Saved!")
        
        
    # The make_dataset method saves and returns the dataset created
    def make_dataset(self,period):
        dataset = self.dataMaker.load_json_candlestick(period)
        self.dataMaker.save_on_file(dataset)
        return dataset