import sys  
sys.path.append('./lib')  
from Dataset_Creator import Dataset_Creator
from Model_Printer import Model_Printer
from Trainer import Trainer
from sklearn.decomposition import PCA 
from sklearn.metrics import mean_absolute_error


#DOWNLOADING DATA AND DATASET BUILDING AND SPLITTING
d = Dataset_Creator ("bitstamp","btcusd")
period="12-h"

training_set, test_set = d.create_dataset(period,True,1)

X_train=training_set[0]
Y_train=training_set[1]
X_test=test_set[0]
Y_test=test_set[1]


#PCA APPLICATION
pca=PCA()
pca.fit(X_train)

X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)


#LIST OF MODELS TO FIT
list_of_models=[[1,0,0,0,0],[2,0,0,0,0],[3,0,0,0,0],[1,1,0,0,0],[2,1,0,0,0],[1,2,0,0,0],[2,2,0,0,0],[1,1,0,0,1],[2,1,0,0,1],[2,2,0,0,1],[2,1,0,0,2],[1,1,1,1,1],[2,1,1,1,1],[2,2,1,1,1],[1,2,1,1,2],[1,2,1,1,1]]


#PRINTS OF LIST OF MODELS TO FIT
mb= Model_Printer ()
mb.print_input_models(list_of_models)


#TRAINING OF MODELS
tr=Trainer ()

tr.train_models(X_train_pca,Y_train,list_of_models)
tr.plot_graphics()
tr.print_models_error()
tr.save_best_estimator()


#BEST MODEL PRINT
print ("The best Model is Model Number {} - Validation Error Rounded: {} Validation Error Full: {}".format(tr.index_of_best_model+1,round(tr.error_of_the_best_model,3),tr.error_of_the_best_model))


#ALGORITHM ERROR	
pred_test=tr.best_model.predict (X_test_pca)
error = mean_absolute_error(pred_test, Y_test)
print ("Final Error of the Algorithm: {} ".format(error))

