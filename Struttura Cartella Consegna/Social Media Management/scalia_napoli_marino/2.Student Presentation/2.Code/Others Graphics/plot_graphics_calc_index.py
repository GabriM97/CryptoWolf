"""
This program allows you to plot the CloseTime vs ClosePrice Graphic and to perform the Indexes Calculation

"""

import sys  
sys.path.append('./lib')  
from Extractor import Extractor as EXTR 
from Time_Stamp_Converter import Time_Stamp_Converter as TSC
from JSON_Saver import JSON_Saver as JSave
from Dataset_Maker import Dataset_Maker as DataMak
from Periods_Maker import Periods_Maker as PM
from Dataset_Creator import Dataset_Creator as DC
from Graph import Graph
from Index import Index
    
#It Plots the graph Timestamp vs ClosePrice  
def graph_plot():
    exchange = "bitstamp"
    pair = "btcusd"
    period = "12-h"
    
    creator = DC(exchange, pair)
    training_set, test_set = creator.create_dataset(period, updated=True)
    
    graph = Graph(exchange, pair, period)
    graph.plotCryptoChart()
    
#It Calculates some Statistics Indexes
def index():
    idx = Index("bitstamp", "btcusd", "12-h")
    candle_matrix, closePrice_matrix = idx.create_matrix()
    openPrice_ar, closePrice_ar = idx.create_np_array(candle_matrix, closePrice_matrix)
    print("Check openPrice_ar and candle_matrix: ", openPrice_ar == candle_matrix[:,2]) #EXPECTED true
    print("Check closePrice_ar and closePrice_matrix: ", closePrice_ar == closePrice_matrix) #EXPECTED true
    print("openPrice_ar shape: ", openPrice_ar.shape)
    print("closePrice_ar: ", closePrice_ar.shape)
    op_mean, cp_mean, op_q0, op_q1, op_q2, op_q3, op_q4, cp_q0, cp_q1, cp_q2, cp_q3, cp_q4, corrMatrix = idx.index(openPrice_ar, closePrice_ar)
    idx.print_dotplot(openPrice_ar, closePrice_ar, op_mean, cp_mean, op_q0, op_q1, op_q2, op_q3, op_q4, cp_q0, cp_q1, cp_q2, cp_q3, cp_q4)
    idx.scatterplot(openPrice_ar, closePrice_ar)
    idx.correlationMatrix(corrMatrix)
    

#  ------  MAIN  ------
graph_plot()
index()   

