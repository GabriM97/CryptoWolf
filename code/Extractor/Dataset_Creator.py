"""
This class helps to create the Dataset.
An instance of this class is unique for the exchange and the pair.
With this object it's possible generate datasets for each passed period via parameter

"""

from JSON_Saver import JSON_Saver as JSave
from Dataset_Maker import Dataset_Maker as DM
from Periods_Maker import Periods_Maker as PM
from Cleaner import Cleaner as CLN
from sklearn.model_selection import train_test_split
import os
import pickle


class Dataset_Creator:
    
    def __init__(self, exchange, pair):        
        self.exchange = exchange
        self.pair = pair
        
        self.jsav = JSave()
        self.periodMaker = PM()
        self.dataMaker = DM(exchange, pair)


    # The create_dataset method allows to create and save a clean dataset. It returns training-set and test-set.
    # Insert cleaning_type=0 (default) to apply a FEATURE SCALING cleaning type
    # Insert cleaning_type=1 to apply a MEAN NORMALIZATION cleaning type
    # The parameter "updated" if it's "True" (default) will download new candlesticks used for the Dataset
    # If it's "False" will create the dataset with the last downloaded candlesticks
    def create_dataset(self, period, updated=True, cleaning_type=0):
        periods_list = self.periodMaker.ret_diz()
        self.period = periods_list[period]
        self.clean = CLN(self.exchange, self.pair, self.period)
        
        if updated:
            self.save_json()
        
        dirty_dataset = self.make_dataset()
        #self.dataMaker.print_data(dirty_dataset)
        
        if cleaning_type == 0:
            self.dataset = self.clean.feature_scaling(dirty_dataset)
        elif cleaning_type == 1:
            self.dataset = self.clean.mean_normalization(dirty_dataset)
        else:
            print("\nValue of cleaning_type error. Dafault cleaning will be applied.")
            self.dataset = self.clean.feature_scaling(dirty_dataset)
        
        X_train, X_test, y_train, y_test = self.split_and_save(self.dataset, 0.30)
        
        return (X_train, y_train), (X_test, y_test)
    
    
    # The save_json method downloads and saves the json files
    def save_json(self):
        date = self.jsav.make_date(1,1,2011,0,0)
        self.jsav.save_on_file(self.exchange, self.pair, date)
        print("Candles Stick Saved!")
        
        
    # The make_dataset method saves and returns the dataset created
    def make_dataset(self):
        dataset = self.dataMaker.load_json_candlestick(self.period)
        self.dataMaker.save_on_file(dataset)
        return dataset
    
    
    # The split_and_save method splits the dataset in Training-set and Test-set
    # and then saves the dataset on file
    def split_and_save(self, dataset, percent):
        X_candles = dataset[1] 
        y_closeP = dataset[0]
        
        # sklearn method
        X_train, X_test, y_train, y_test = train_test_split(X_candles, y_closeP, test_size=percent, shuffle=False)
        
        training_set = (X_train, y_train)
        test_set = (X_test, y_test)
        self.save_on_file(training_set, test_set)
        print("\nTraining-set and Test-set created!")
        
        return X_train, X_test, y_train, y_test
        
    
    # The save_on_file method allows to save training and test on file
    def save_on_file(self, training, test):
        x_train = training[0]
        y_train = training[1]
        self.save(x_train, y_train, "training-set")
        #print("\nTraining-set saved!")
        
        x_test = test[0]
        y_test = test[1]
        self.save(x_test, y_test, "test-set")
        #print("\nTest-set saved!")

    # The save method creates the filepath and saves X_set and y_set on a ".plk" file. It will create directories if the filepath doesn't exists
    def save(self, x_set, y_set, type_set):        
        plk_file = "{}_{}.plk".format(self.period, type_set)
        directory = "{}/{}/dataset/".format(self.exchange, self.pair)

        if not os.path.exists(directory):
            os.makedirs(directory)

        filepath = "{}{}".format(directory, plk_file)
        with open(filepath, "wb") as out:
            pickle.dump({
                    'X_set': x_set,
                    'y_set': y_set,
            },out)
