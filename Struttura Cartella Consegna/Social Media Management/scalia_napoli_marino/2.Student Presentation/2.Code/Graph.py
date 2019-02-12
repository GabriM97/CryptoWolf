"""
This class allows to plot the chart CloseTime vs ClosePrice

"""

from Periods_Maker import Periods_Maker as PM
from matplotlib import pyplot as plt
import pickle

class Graph:
    
    def __init__(self, exchange, pair, period):
        self.exchange = exchange
        self.pair = pair
        self.period = period
        self.periodMaker = PM()
        
    # The getDataset method allows to open the dataset from file
    def getDataset(self):
        periods_list = self.periodMaker.ret_diz()
        self.period = periods_list[self.period]
        
        filepath = "{}/{}/plk/{}.plk".format(self.exchange, self.pair, self.period) 
        with open(filepath, "rb") as inp:
            dataset = pickle.load(inp)
        return dataset
    
    # The plotCryptoGraph method plots the graph Timestamp vs ClosePrice
    def plotCryptoChart(self):
        plt.figure(figsize=(15,5))
        plt.subplot(1,1,1)
        
        dataset = self.getDataset()        
        closeTime = dataset.get("candlestick_matrix")[:,0]
        closePrice = dataset.get("closePrice_matrix")
        
        plt.plot(closeTime, closePrice, linewidth=1, c='blue', label="BTC Price")
        frame = plt.gca()
        plt.legend(loc='upper left')
        
        plt.grid(True)
        plt.rc('grid', linestyle=":", linewidth=1, color='gray')
        
        frame.axes.get_xaxis().set_visible(False)
        plt.xlabel("Timestamp")
        plt.ylabel("Price $")
        plt.title("{} Chart".format(self.pair.upper()))
        plt.show()
