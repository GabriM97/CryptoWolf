"""
This class will create a pair of matrices for each periods of candlestick. This two matrices will be our Dataset

"""

import json
import pickle
import os
from Periods_Maker import Periods_Maker as PM
from Time_Stamp_Converter import Time_Stamp_Converter as TSC

class Dataset_Maker:

    def __init__(self, exchange, pair):
       self.filepath = "{}/{}/".format(exchange, pair)
       self.exchange = exchange
       self.pair = pair
       self.container = dict()


    # The extract method returns the content of the json file
    def extract(self):
        json_file = "{}json/{}.json".format(self.filepath, self.period) 
        with open(json_file, "rb") as inp:
            data = json.load(inp)
        return data


    # This method reads the json file and creates the pair of matrices that will contains info about candlesticks of a single period
    # The two matrices are managed as a tuple in the "container" variable that will be our dataset
    def load_json_candlestick(self, period):
        self.period = period
        data = self.extract()
        candles = data[self.period]

        candles_matrix = list()
        close_matrix = []

        for i in range(len(candles)):
            row, closePrice = self._make_data(candles,i)
            candles_matrix.append(row)
            close_matrix.append(closePrice)

        self.container = (close_matrix, candles_matrix)
        return self.container


    # The _make_data method returns a record for the candlestick matrix and a record for the close-price matrix
    # (Part of load_json_candlestick method)
    def _make_data(self, candles, index):
        row = list()
        candle = candles[index]
        
        row.append(candle[0])           # Close Time
        row.append(round(candle[1],2))  # Open Price
        row.append(round(candle[2],2))  # High Price
        row.append(round(candle[3],2))  # Low Price
        row.append(round(candle[5],2))  # Volume
        
        closePrice = round(candle[4],2)
        return row, closePrice


    # The print_data method prints an output for each candlestick      output format: [TIMESTAMP - PRICE - VOLUME]
    def print_data(self, dataset):
        candles = dataset[1]
        close_matrix = dataset[0]
        per_mak = PM()
        periods_list = per_mak.ret_rev_diz()
        output_period = periods_list[self.period]
        tsc = TSC()
        
        for i in range(len(candles)):
            print("{}\t".format(tsc.get_date(candles[i][0])), end="")
            print("${}\t\t".format(int(close_matrix[i])), end="")
            print("BTC {}".format(round(candles[i][4],2)))

        print("\n"+ self.exchange.title() +" - "+ self.pair.upper())
        print("Candles Stick Period:", output_period)


    # The save_on_file method allows to save the dataset on file
    def save_on_file(self, dataset):
        if len(dataset) >= 1:
            closePrice_matrix = dataset[0]
            candlestick_matrix = dataset[1]
            self.save(candlestick_matrix, closePrice_matrix, self.period)
            print("\nMatrixs saved")
        else:
           print("\nError! Nothing to save!")


    # The save method creates the filepath and saves the dataset on a ".plk" file. It will create directories if the filepath doesn't exists
    def save(self, candles, closePrices, period):
        plk_file = "{}.plk".format(self.period)
        directory = "{}plk/".format(self.filepath)

        if not os.path.exists(directory):
            os.makedirs(directory)

        self.filepath = "{}{}".format(directory, plk_file)
        with open(self.filepath, "wb") as out:
            pickle.dump({
                    'candlestick_matrix': candles,
                    'closePrice_matrix': closePrices,
            },out)