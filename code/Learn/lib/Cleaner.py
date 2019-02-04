"""
This class clean the features with "Mean Normalization" and "Feature Scaling"

"""

import numpy as np
import os
import pickle
from Periods_Maker import Periods_Maker as PM

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
        
        self.save_feature_scaling_max(closeP, timestamp, openP, highP, lowP, volume)

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
     
        
    # The save_feature_scaling_max method saves on a plk file the maximum features value
    def save_feature_scaling_max(self, closeP, timestamp, openP, highP, lowP, volume):
        plk_file = "{}_feature_scaling_max.plk".format(self.period)
        #directory = "{}plk/".format(self.filepath)
        directory = "./lib"

        if not os.path.exists(directory):
            os.makedirs(directory)

        filepath = "{}/{}".format(directory, plk_file)
        with open(filepath, "wb") as out:
            pickle.dump({
                    'closePrice': max(closeP),
                    'closeTime': max(timestamp),
                    'openPrice': max(openP),
                    'highPrice': max(highP),
                    'lowPrice': max(lowP),
                    'volume': max(volume),
            },out)
    
    
    # The open_feature_scaling_max method returns the maximum feature values from the saved plk file 
    def open_feature_scaling_max(self):
        periodMaker = PM()
        periods_list = periodMaker.ret_diz()
        self.period = periods_list[self.period]
	
        filepath = "./lib/{}_feature_scaling_max.plk".format(self.period) 
        with open(filepath, "rb") as inp:
            fs_max = pickle.load(inp)
            
        closePrice = fs_max.get("closePrice")
        closeTime = fs_max.get("closeTime")
        openPrice = fs_max.get("openPrice")
        highPrice = fs_max.get("highPrice")
        lowPrice = fs_max.get("lowPrice")
        volume = fs_max.get("volume")
            
        return closePrice, closeTime, openPrice, highPrice, lowPrice, volume
    
    
    # The mean_normalization method returns (and saves on file) a new dataset with each normalized feature 
    def mean_normalization(self, dataset):
        closeP, timestamp, openP, highP, lowP, volume = self._getData(dataset)
        
        self.save_mean_norm_info(closeP, timestamp, openP, highP, lowP, volume)
        
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
    
    
    # The save_mean_norm_info method saves on a plk file the maximum and the mean features value
    def save_mean_norm_info(self, closeP, timestamp, openP, highP, lowP, volume):
        plk_file = "{}_mean_norm_info.plk".format(self.period)
        #directory = "{}plk/".format(self.filepath)
        directory = "./lib"

        if not os.path.exists(directory):
            os.makedirs(directory)

        filepath = "{}/{}".format(directory, plk_file)
        with open(filepath, "wb") as out:
            pickle.dump({
                    'closePrice': (max(closeP), int(closeP.mean())),
                    'closeTime': (max(timestamp), int(timestamp.mean())),
                    'openPrice': (max(openP), int(openP.mean())),
                    'highPrice': (max(highP), int(highP.mean())),
                    'lowPrice': (max(lowP), int(lowP.mean())),
                    'volume': (max(volume), int(volume.mean())),
            },out)
    
    
    # The open_mean_norm_info method returns tuples of the maximum and the mean feature values from the saved plk file
    def open_mean_norm_info(self):
        periodMaker = PM()
        periods_list = periodMaker.ret_diz()
        self.period = periods_list[self.period]
        
        filepath = "./lib/{}_mean_norm_info.plk".format(self.period) 
        with open(filepath, "rb") as inp:
            fs_max = pickle.load(inp)
            
        closePrice = fs_max.get("closePrice")
        closeTime = fs_max.get("closeTime")
        openPrice = fs_max.get("openPrice")
        highPrice = fs_max.get("highPrice")
        lowPrice = fs_max.get("lowPrice")
        volume = fs_max.get("volume")
            
        return closePrice, closeTime, openPrice, highPrice, lowPrice, volume
        

    # The save method creates the filepath and saves the scaled dataset on a ".plk" file. It will create directories if the filepath doesn't exists
    def save(self, candles, closePrices):
        plk_file = "{}_cleaned.plk".format(self.period)
        directory = "{}plk/".format(self.filepath)

        if not os.path.exists(directory):
            os.makedirs(directory)

        filepath = "{}{}".format(directory, plk_file)
        with open(filepath, "wb") as out:
            pickle.dump({
                    'candlestick_matrix': candles,
                    'closePrice_matrix': closePrices,
            },out)
