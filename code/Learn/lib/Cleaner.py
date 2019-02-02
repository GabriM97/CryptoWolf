"""
This class clean the features with "Mean Normalization" and "Feature Scaling"

"""

import numpy as np
import os
import pickle

class Cleaner:
    
    def __init__(self, exchange, pair, period):
        self.exchange = exchange
        self.pair = pair
        self.period = period
        self.filepath = "{}/{}/".format(exchange, pair)
    
    
    # The _getData method helps to get the single feature to scale
    def _getData(self, dataset):
        close_matrix = dataset[0]   # Close Price
        candles_matrix = dataset[1]
        
        closeTime = candles_matrix[:,0] # First column of the matrix
        openPrice = candles_matrix[:,1]
        highPrice = candles_matrix[:,2]
        lowPrice = candles_matrix[:,3]
        volume = candles_matrix[:,4]    # Last column of the matrix
        
        return close_matrix, closeTime, openPrice, highPrice, lowPrice, volume
    
    
    # The feature_scaling method returns (and saves on file) a new dataset with each scaled feature 
    def feature_scaling(self, dataset):
        closeP, timestamp, openP, highP, lowP, volume = self._getData(dataset)
        
        closeP = closeP/max(closeP)
        timestamp = timestamp/max(timestamp)
        openP = openP/max(openP)
        highP = highP/max(highP)
        lowP = lowP/max(lowP)
        volume = volume/max(volume)
        
        tmp_candles = np.array([timestamp, openP, highP, lowP, volume])
        candles = tmp_candles.T
        
        self.save(candles, closeP)
        return (closeP, candles)
        
    
    # The mean_normalization method returns (and saves on file) a new dataset with each normalized feature 
    def mean_normalization(self, dataset):
        closeP, timestamp, openP, highP, lowP, volume = self._getData(dataset)
        
        closeP = (closeP - int(closeP.mean())) / max(closeP)
        timestamp = (timestamp - int(timestamp.mean())) / max(timestamp)
        openP = (openP - int(openP.mean())) / max(openP)
        highP = (highP - int(highP.mean())) / max(highP)
        lowP = (lowP - int(lowP.mean())) / max(lowP)
        volume = (volume - int(volume.mean())) / max(volume)
        
        tmp_candles = np.array([timestamp, openP, highP, lowP, volume])
        candles = tmp_candles.T
        
        self.save(candles, closeP)
        return (closeP, candles)
        

    # The save method creates the filepath and saves the scaled dataset on a ".plk" file. It will create directories if the filepath doesn't exists
    def save(self, candles, closePrices):
        plk_file = "{}_cleaned.plk".format(self.period)
        directory = "{}plk/".format(self.filepath)

        if not os.path.exists(directory):
            os.makedirs(directory)

        self.filepath = "{}{}".format(directory, plk_file)
        with open(self.filepath, "wb") as out:
            pickle.dump({
                    'candlestick_matrix': candles,
                    'closePrice_matrix': closePrices,
            },out)