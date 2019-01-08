from Model_Printer import Model_Printer
from Trainer import Trainer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_validate
import pickle

#TEST CLASS TRAINER
mb=Model_Printer()
tr=Trainer()

#TRAINING-SET
x=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24],[25,26,27,28],[29,30,31,32],[33,34,35,36],[37,38,39,40]]  

#TRAINING-SET TARGETS
y=[50,32,93,40,62,150,96025,45,30,690] 
	
#MODELS
l=[[1,1,1,1],[1,1,1,2],[1,0,1,2],[1,0,1,0],[1,1,1,1],[1,1,1,2]] 

print("")
print ("--------------MODELS----------------- \n")
mb.print_input_models(l) #VIEW MODELS

print("")
print("")

#TEST CLASS TRAINER - train_models&cross_validation&merge
print ("--------------TRAINING----------------- \n")
tr.train_models (x,y,l) 

print("")
print("")

#TEST CLASS TRAINER - take_the_best_model_from_last_training 
print ("--------------TAKE_THE_BEST_MODEL_FROM_LAST_TRAINING----------------- \n")
tr.take_the_best_model_from_last_training() 
print ("Error Best Model {}".format(tr.error_of_the_best_model))
print("Best Model Features {}".format(tr.best_model_features))
print("Train Error Best Model {}".format(tr.best_train_for_the_best_model))
print ("Best Model Object: \n {}".format(tr.best_model))
print ("Theta-0 Best Model: {} ".format(tr.best_model.intercept_))

print ("")
print("")

#TEST CLASS TRAINER - save_best_estimator
tr.save_best_estimator()

with open("best_model_features.pkl", "rb") as inp:
	data=pickle.load(inp)

with open("best_model.pkl", "rb") as inp:
	data_2=pickle.load(inp)

print ("--------------SAVE_BEST_ESTIMATOR----------------- \n")
print ("Best Model Features Saved {}".format(data['Best_F']))
print ("Best Model Object Saved: \n {} ".format(data_2['Best_M']))
print ("Theta-0 Saved Best Model: {} ".format(data_2['Best_M'].intercept_))

print ("")
print("")

#TEST CLASS TRAINER - are_equals
l1=[1,1,1]
l2=[1,1,1]
l3=[1,2,2]
l4=[0,1,2]
l5=[0,2,2]
print ("--------------ARE_EQUALS----------------- \n")
print ("Are Equals l1 vs l2: {}".format(tr.are_equals(l1,l2))) #EXPECTED 2
print ("Are Equals l1 vs l3: {}".format(tr.are_equals(l1,l3))) #EXPECTED 1
print ("Are Equals l1 vs l4: {}".format(tr.are_equals(l1,l4))) #EXPECTED 0
print ("Are Equals l4 vs l5: {}".format(tr.are_equals(l4,l5))) #EXPECTED 1

print ("")
print("")

#TEST CLASS TRAINER - take_degree
print ("--------------TAKE_DEGREE----------------- \n")
print ("Degree l5: {}".format(tr.take_degree(l5))) #EXPECTED 2
print ("Degree l1: {}".format(tr.take_degree(l1))) #EXPECTED 1


print ("")
print("")

#TEST CLASS TRAINER - print_models_error
print ("--------------MODELS_ERRORS----------------- \n")
tr.print_models_error() 

#TEST CLASS TRAINER - plot_graphics
tr.plot_graphics() 



