from Dataset_Projector import Dataset_Projector 
from sklearn.model_selection import cross_validate
from sklearn.linear_model import LinearRegression
import pickle
import cPickle
import Curve

class Trainer:

	def train_models (self,path_del_file_pkl_del_training_set, lista_delle_proiezioni #QUESTA STRUTTURA È UNA LISTA DI LISTE):	

		self.j_train=list()
		self.j_cv=list()
		self.estimators=list()

		self.projections=lista_delle_proiezioni
		self.best_model_features=list()

		CARICO IL TRAINING SET DAL FILE PKL E LO POSIZIONO NELLE VARIABILI: X_Train, Y_Train	

		proiettore=Dataset_Projector ()	
		lista_dei_dataset_proiettati=list()	

		for i in range( len(lista_delle_proiezioni)):
			lista_dei_dataset_proiettati.append(proiettore.to_project (X_Train, lista_delle_proiezioni [i]))

		for i in range( len(lista_dei_dataset_proiettati)):
			estimator=LinearRegression()
			cv_results = cross_validate(estimator, lista_dei_dataset_proiettati[i], Y_Train,scoring="neg_mean_absolute_error" cv=5,return_train_score=True,return_estimator=True)

			self.j_train.append(cv_results['train_score'])
			self.j_cv.append(cv_results['test_score'])	
			self.estimators.append(cv_results['estimator'])	

		print ("Training Ended \n")

	def take_the_best_model_from_last_training (self):
		best_cv_for_every_model=list()

		for i in range (self.j_cv):
			best_cv_for_every_model.append(min(self.j_cv[i]))

		best_model= best_cv_for_every_model.index(min(best_cv_for_every_model))

		self.error_of_the_best_model= best_cv_for_every_model[best_model]
		self.best_model= self.estimator[best_model]
		self.best_model_features=self.projections[best_model]
		best_train_for_the_best_model=min (self.j_train[best_model])

		return self.error_of_the_best_model, self.best_model, self.best_model_features, best_train_for_the_best_model
		#RESTITUISCO IL MIGLIOR MODELLO ASSIEME AL SUO ERRORE J-CV, ALLE SUE FEATURES E AL SUO ERRORE DI TRAINING

	def save_best_estimator (self):

		self.take_the_best_model_from_last_training()
		best_model = open('best_model.obj', 'w')
		pickle.dump(self.best_model, best_model)

		best_model = open('best_model_features.obj', 'w')
		pickle.dump(self.best_model_features, best_model_features)	

	def plot_graphics (self):
		[.....]	


				
