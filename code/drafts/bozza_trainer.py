from Dataset_Projector import Dataset_Projector 
from sklearn.model_selection import cross_validate
from sklearn.linear_model import LinearRegression
import pickle
import cPickle
import Curve
import Record_Degree

class Trainer:

	def train_models (self,path_del_file_pkl_del_training_set, lista_delle_proiezioni #QUESTA STRUTTURA È UNA LISTA DI LISTE):	

		self.j_train=list() #LISTA DI LISTE CONTENENTE GLI ERRORI DI TRAINING
		self.j_cv=list() #LISTA DI LISTE CONTENENTE GLI ERRORI DI CONVALIDATION
		self.estimators=list() #LISTA DI LISTE CONTENENTE GLI ESTIMATORI
		self.rec_deg=list () #LISTA DEI RECORD DEI GRADI
		self.projections=lista_delle_proiezioni #LISTA DI LISTE CONTENENTE TUTTI I MODELLI PRESENTI NELL'ULTIMO ALLENAMENTO
		self.best_model_features=list() #LISTA CONTENENTE LE FEATURES DEL MIGLIOR ESTIMATORE
		self.activated_index=0 #VARIABILE CHE FA SCATTARE UK RECORDER_DEGREE

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
			
			if (i>0):
				if (are_equals(lista_delle_proiezioni[i],lista_delle_proiezioni[i-1]) ==True):
					if (self.activated_index==0):
						ob=Recorder_Degree()
						self.rec_deg.append(ob)

						self.rec_deg[-1].record(take_degree(lista_delle_proiezioni[i-1]),min(self.j_train[i-1]),min (self.j_cv[i-1]))
						self.rec_deg[-1].record(take_degree(lista_delle_proiezioni[i]),min(self.j_train[i]),min (self.j_cv[i]))
						self.activated_index=5
					else:
						self.rec_deg[-1].record(take_degree(lista_delle_proiezioni[i]),min(self.j_train[i]),min (self.j_cv[i]))
				else:
					self.activated_index=0	

		
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

	def are_equals (self,m_1,m_2):
		[...]

	def take_degree (self,modello):
		[...]


				
