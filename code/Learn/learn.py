import sys  
sys.path.append('./lib')  
from Dataset_Creator import Dataset_Creator
from Model_Printer import Model_Printer
from Trainer import Trainer
from sklearn.decomposition import PCA 
from sklearn.metrics import mean_absolute_error
import pickle
from Dataset_Projector import Dataset_Projector

#THIS FUNCTION SAVES THE PCA OBJECT INTO A PLK FILE
def save_pca (pca):
	plk = "pca.plk"
	direc = "./"
	
	filepath = "{}{}".format(direc,plk)

	with open (filepath,"wb") as out:
		pickle.dump ( { 'pca':pca } ,out)


print ("\n\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<LEARN>>>>>>>>>>>>>>>>>>>>>>\n")

#PARIMITERS CHOICES
graph=False
update=True
model_list_complete=0
pca_apply=1
try:	

	print ("\n\n********************TRAINING-SETUP************************\n")


	print ("1) Download/Update Data ?\n Insert: \n -> 0 - Use local data  \n -> 1 - Download/Update data from the internet")
	answer=int(input ("\n -> "))
	if ((answer !=0) and (answer!=1)):
		print ("Error, you have to insert 0 or 1")
		exit (3)
	update=answer
	print("")


	print ("2) Plot graphics ?\n Insert: \n -> 0 - Do not plot Training Graphics\n -> 1 - Plot Training Graphics")
	answer=int(input ("\n -> "))
	if (answer !=0 and answer!=1):
		print ("Error, you have to insert 0 or 1")
		exit (3)
	graph=answer
	print("")

	print ("3) Do you want the full model list (144 models) for the Training ?\n Insert: \n -> 0 - No, use restricted list\n -> 1 - Yes, use Full List\n")
	answer=int(input ("\n -> "))
	if (answer !=0 and answer!=1):
		print ("Error, you have to insert 0,1 or 2")
		exit (3)
	model_list_complete=answer
	print("")


	print ("4) Do you want to apply the pca on the dataset?\n Insert: \n -> 0 - No, don't apply it\n -> 1 - Yes, apply PCA\n")
	answer=int(input ("\n -> "))
	if (answer !=0 and answer!=1):
		print ("Error, you have to insert 0,1 or 2")
		exit (3)
	pca_apply=answer
	print("")


except ValueError:
	print ("Error, You have to insert a numeric value")
	exit (2)


print ("\n\n********************DATASET-BUILDING-AND-SPLITTING********************\n")
#DOWNLOADING DATA AND DATASET BUILDING AND SPLITTING
d = Dataset_Creator ("bitstamp","btcusd")
period="12-h"

training_set, test_set = d.create_dataset(period,update)

X_train=training_set[0]
Y_train=training_set[1]
X_test=test_set[0]
Y_test=test_set[1]

#PCA APPLICATION
if (pca_apply==1):

	pca=PCA()
	pca.fit(X_train)

	X_train = pca.transform(X_train)
	X_test = pca.transform(X_test)


#LIST OF MODELS TO FIT
if (model_list_complete==1):

	list_of_models=[ [1,0,0,0,0],[2,0,0,0,0],[3,0,0,0,0], [ 0,1,0,0,0 ],[ 0,2,0,0,0 ],[ 0,3,0,0,0 ], [0,0,1,0,0],[0,0,2,0,0],[0,0,3,0,0], [0,0,0,1,0],[0,0,0,2,0],[0,0,0,3,0], [0,0,0,0,1],[0,0,0,0,2],[0,0,0,0,3],  [1,1,0,0,0], [2,1,0,0,0], [1,2,0,0,0], [2,2,0,0,0], [3,1,0,0,0], [1,0,1,0,0],[2,0,1,0,0],[1,0,2,0,0],[2,0,2,0,0],[3,0,1,0,0],[1,0,0,1,0], [2,0,0,1,0],[1,0,0,2,0],[2,0,0,2,0],[3,0,0,1,0],[1,0,0,0,1],[2,0,0,0,1],[1,0,0,0,2],[2,0,0,0,2],[3,0,0,0,1], [0,1,1,0,0],[0,2,1,0,0],[0,1,2,0,0],[0,2,2,0,0],[0,3,1,0,0], [0,1,0,1,0],[0,2,0,1,0],[0,1,0,2,0],[0,2,0,2,0],[0,3,0,1,0], [0,1,0,0,1],[0,2,0,0,1],[0,1,0,0,2],[0,2,0,0,2],[0,3,0,0,1], [0,0,1,1,0],[0,0,2,1,0],[0,0,1,2,0],[0,0,2,2,0],[0,0,3,1,0], [0,0,1,0,1],[0,0,2,0,1],[0,0,1,0,2], [0,0,2,0,2],[0,0,3,0,1], [0,0,0,1,1],[0,0,0,2,1],[0,0,0,1,2],[0,0,0,2,2],[0,0,0,3,1],[1,1,1,0,0], [2,1,1,0,0], [1,2,1,0,0], [2,2,1,0,0], [3,1,1,0,0], [1,1,0,1,0], [2,1,0,1,0], [1,2,0,1,0], [2,2,0,1,0], [3,1,0,1,0], [1,1,0,0,1], [2,1,0,0,1], [1,2,0,0,1], [2,2,0,0,1],[3,1,0,0,1], [1,0,1,1,0], [2,0,1,1,0], [1,0,2,1,0],[2,0,2,1,0], [3,0,1,1,0], [1,0,1,0,1], [2,0,1,0,1], [1,0,2,0,1], [2,0,2,0,1], [3,0,1,0,1], [1,0,0,1,1],[2,0,0,1,1],[1,0,0,2,1],[2,0,0,2,1],[3,0,0,1,1],[0,1,1,1,0],[0,2,1,1,0],[0,1,2,1,0],[0,2,2,1,0],[0,3,1,1,0],[0,1,1,0,1],[0,2,1,0,1],[0,1,2,0,1],[0,2,2,0,1],[0,3,1,0,1],[0,1,0,1,1], [0,2,0,1,1],[0,1,0,2,1],[0,2,0,2,1],[0,3,0,1,1],[0,0,1,1,1],[0,0,2,1,1], [0,0,1,2,1],[0,0,2,2,1],[0,0,3,1,1], [1,1,1,1,0],[2,1,1,1,0],[1,2,1,1,0],[2,2,1,1,0],[3,1,1,1,0],[1,1,1,0,1],[2,1,1,0,1],[1,2,1,0,1],[2,2,1,0,1],[3,1,1,0,1],[1,1,0,1,1], [2,1,0,1,1],[1,2,0,1,1],[2,2,0,1,1],[3,1,0,1,1],[1,0,1,1,1],[2,0,1,1,1],[1,0,2,1,1],[2,0,2,1,1],[3,0,1,1,1], [0,1,1,1,1],[0,2,1,1,1],[0,1,2,1,1], [0,2,2,1,1], [0,3,1,1,1], [1,1,1,1,1], [2,1,1,1,1], [2,2,1,1,1], [3,1,1,1,1], ]

else:
	list_of_models=[[1,0,0,0,0],[2,0,0,0,0],[3,0,0,0,0],[1,1,0,0,0],[2,1,0,0,0],[1,2,0,0,0],[2,2,0,0,0],[1,1,0,0,1],[2,1,0,0,1],[2,2,0,0,1],[2,1,0,0,2],[1,1,1,1,1],[2,1,1,1,1],[2,2,1,1,1],[1,2,1,1,2],[1,2,1,1,1]]


print ("\n\n********************MODELS-LIST********************\n")
#PRINTS OF LIST OF MODELS TO FIT
mb= Model_Printer ()
mb.print_input_models(list_of_models)


print ("\n\n********************TRAINING********************\n")
#TRAINING OF MODELS
tr=Trainer ()

tr.train_models(X_train,Y_train,list_of_models)
if (graph==True):
	tr.plot_graphics()


print ("\n\n********************TRAINING-ERROS********************\n")
tr.print_models_error()
tr.save_best_estimator()


print ("\n\n********************BEST-MODEL********************\n")
#BEST MODEL PRINT
print ("The best Model is Model Number {} - Validation Error Rounded: {} Validation Error Full: {}".format(tr.index_of_best_model+1,round(tr.error_of_the_best_model,3),tr.error_of_the_best_model))


print ("\n\n********************FINAL-ERROR********************\n")
#ALGORITHM ERROR
projector=Dataset_Projector()
X_test=	projector.to_project(X_test,list_of_models[tr.index_of_best_model])
pred_test=tr.best_model.predict (X_test)
error = mean_absolute_error(pred_test, Y_test)
print ("Final Error of the Algorithm: {} \n".format(error))


#SAVE PCA
if (pca_apply==1):

	save_pca(pca)

