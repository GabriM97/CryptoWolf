"""
This class plots statistical index.
The input is a matrix from the method make_dataset(self) of Dataset_Creator class

"""

from Periods_Maker import Periods_Maker as PM
from matplotlib import pyplot as plt
import statsmodels.graphics.api as smg
import scipy.stats as stats
import numpy as np
import pickle

class Index:
    
    def __init__ (self, exchange, pair, period):
        self.pair = pair;
        self.exchange = exchange;
        self.period = period;
        self.periodMaker = PM()

#This method extracts dataaset from file previously created. Dataset is a tuple
    def getDataset(self):
        periods_list = self.periodMaker.ret_diz()
        self.period = periods_list[self.period]
        filepath = "{}/{}/plk/{}.plk".format(self.exchange, self.pair, self.period)
        with open(filepath, "rb") as inp:
            dataset = pickle.load(inp)
        return dataset
        
#This method creates two matrices (candle and close price) from dataset
    def create_matrix (self):
        dataset = self.getDataset()
        candle = dataset.get("candlestick_matrix")
        closePrice = dataset.get("closePrice_matrix")
        return candle, closePrice
    
#This method converts the matrices in numpy arrays
    def create_np_array(self, candle_matrix, closePrice_matrix):
        openPrice_ar = np.array(candle_matrix[:,2])
        closePrice_ar = np.array(closePrice_matrix)
        return openPrice_ar, closePrice_ar
        
#This method computes statistical indexes and returns some useful indexes for graphs
    def index(self, openPrice_ar, closePrice_ar):
        op_min = openPrice_ar.min()
        print("Open Price Minimum: ", op_min)
        cp_min = closePrice_ar.min()
        print("Close Price Minimum: ", cp_min)
        op_max = openPrice_ar.max()
        print("Open Price Maximum: ", op_max)
        cp_max = closePrice_ar.max()
        print("Close Price Maximum: ", cp_max)
        op_range = openPrice_ar.max()-openPrice_ar.min()
        print("Open Price Range: ", op_range)
        cp_range = closePrice_ar.max()-closePrice_ar.min()
        print("Close Price Range: ", cp_range)
        op_mean = openPrice_ar.mean()
        print("Open Price Mean: ", op_mean)
        cp_mean = closePrice_ar.mean()
        print("Close Price Mean: ", cp_mean)
        op_median = np.median(openPrice_ar)
        print("Open Price Median: ", op_median)
        cp_median = np.median(closePrice_ar)
        print("Close Price Median: ", cp_median)
        op_q0, op_q1, op_q2, op_q3, op_q4 = np.percentile(openPrice_ar, [0, 25, 50, 75, 100])
        print("Minimum Open Price: ", op_q0)
        print("1/4 of Open Price: ", op_q1)
        print("1/2 of Open Price: ", op_q2)
        print("3/4 of Open Price: ", op_q3)
        print("Maximum Open Price: ", op_q4)
        cp_q0, cp_q1, cp_q2, cp_q3, cp_q4 = np.percentile(closePrice_ar, [0, 25, 50, 75, 100])
        print("Minimum Open Price: ", cp_q0)
        print("1/4 of Open Price: ", cp_q1)
        print("1/2 of Open Price: ", cp_q2)
        print("3/4 of Open Price: ", cp_q3)
        print("Maximum Open Price: ", cp_q4)
        op_variance = np.var(openPrice_ar)
        print("Open Price Variance: ", op_variance)
        cp_variance = np.var(closePrice_ar)
        print("Close Price Variance: ", cp_variance)
        op_std = np.std(openPrice_ar)
        print("Open Price STD: ", op_std)
        cp_std = np.std(closePrice_ar)
        print("Close Price STD: ", cp_std)
        covariance = np.cov(openPrice_ar, closePrice_ar)
        print("Covariance: ", covariance)
        pearson = stats.pearsonr(openPrice_ar, closePrice_ar)
        print("Pearson's Index: ", pearson)
        spearman = stats.spearmanr(openPrice_ar, closePrice_ar)
        print("Spearman's Index: ", spearman)
        corrMatrix = np.corrcoef(openPrice_ar, closePrice_ar)
        print("Correlation Matrix: ", corrMatrix)
        kendall = stats.kendalltau(openPrice_ar, closePrice_ar)
        print("Kendall Index: ", kendall)
        return op_mean, cp_mean, op_q0, op_q1, op_q2, op_q3, op_q4, cp_q0, cp_q1, cp_q2, cp_q3, cp_q4, corrMatrix

#This service function sets up dotplot    
    def _make_dotplot(self, x, title='Dotplot'):
        plt.plot(x, np.random.random(x.shape), 'o')
        plt.title(title)
        plt.yticks([])

#This method plots dotplot 
    def print_dotplot(self, openPrice_ar, closePrice_ar, op_mean, cp_mean, op_q0, op_q1, op_q2, op_q3, op_q4, cp_q0, cp_q1, cp_q2, cp_q3, cp_q4):
        plt.figure(figsize = (18, 8))
        plt.subplot(311)
        self._make_dotplot(openPrice_ar, title='Open Price')
        plt.plot([op_mean, op_mean], [0,1], 'r')
        plt.plot([op_q0, op_q0], [0,1], linewidth=3)
        plt.plot([op_q1, op_q1], [0,1], linewidth=3)
        plt.plot([op_q2, op_q2], [0,1], linewidth=3)
        plt.plot([op_q3, op_q3], [0,1], linewidth=3)
        plt.plot([op_q4, op_q4], [0,1], linewidth=3)
        plt.legend(['Points', 'Mean', 'Q0', 'Q1', 'Q2', 'Q3', 'Q4'])
        plt.subplot(312)
        self._make_dotplot(closePrice_ar, title='Close Price')
        plt.plot([cp_mean, cp_mean], [0,1], 'r')
        plt.plot([cp_q0, cp_q0], [0,1], linewidth=3)
        plt.plot([cp_q1, cp_q1], [0,1], linewidth=3)
        plt.plot([cp_q2, cp_q2], [0,1], linewidth=3)
        plt.plot([cp_q3, cp_q3], [0,1], linewidth=3)
        plt.plot([cp_q4, cp_q4], [0,1], linewidth=3)
        plt.legend(['Points', 'Mean', 'Q0', 'Q1', 'Q2', 'Q3', 'Q4'])
        plt.show
        
    def scatterplot(self, openPrice_ar, closePrice_ar):
        plt.figure(figsize = (8, 8))
        plt.scatter(openPrice_ar, closePrice_ar)
        plt.title("ScatterPlot")
        plt.show()
        
    def correlationMatrix(self, corr):
        smg.plot_corr(corr, xnames=["Open Price", "Close Price"], normcolor=True)
        plt.show()
        
