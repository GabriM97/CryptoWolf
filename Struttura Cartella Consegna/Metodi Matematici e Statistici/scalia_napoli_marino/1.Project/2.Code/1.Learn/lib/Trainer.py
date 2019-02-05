"""

This class allow you to train a series of Models in a simultanius way

"""

from Dataset_Projector import Dataset_Projector
from sklearn.linear_model import LinearRegression
import pickle
from Curve import Curve
from Recorder_Degree import Recorder_Degree
from sklearn.model_selection import KFold
import numpy as np
from sklearn.metrics import mean_absolute_error

class Trainer:

	#The train_models method fits a series of models passed in input
	def train_models (self,X_Train,Y_Train,models_list):
		self.j_train=list() 
		self.j_cv=list() 
		self.regressors=list() 
		self.rec_deg=list() 
		self.models=models_list
		self.best_model_features=list()
		self.activated_serie=0
		projector=Dataset_Projector()
		self.list_of_projected_dataset=list()
		self.y=Y_Train

		for i in range (len(models_list)):
			self.j_train.append(list())
			self.j_cv.append (list())
			self.regressors.append (list())

		for i in range (len(models_list)):
			self.list_of_projected_dataset.append(projector.to_project(X_Train,models_list[i]))

		for i in range (len(models_list)):
			self.cross_validation(self.list_of_projected_dataset[i],Y_Train,5,i)

			if (i>0):
				if (self.are_equals(models_list[i],models_list[i-1])==1 or self.are_equals(models_list[i],models_list[i-1])==2):
					if (self.activated_serie==0):
						ob=Recorder_Degree()
						self.rec_deg.append(ob)

						self.rec_deg[-1].record (self.take_degree(models_list[i-1]),min(self.j_train[i-1]),min (self.j_cv[i-1]),i-1)
						self.rec_deg[-1].record (self.take_degree(models_list[i]),min(self.j_train[i]),min (self.j_cv[i]),i)	

						self.activated_serie=5
					else:
						self.rec_deg[-1].record (self.take_degree(models_list[i]),min(self.j_train[i]),min (self.j_cv[i]),i)	
				elif (self.are_equals(models_list[i],models_list[i-1]) ==0):
					self.activated_serie=0

		print ("Training Ended \n")

	#The cross-validation method implements the "Cross-Validation" technque
	def cross_validation (self,X_Train,Y_Train,k,idx):
		
		x=list()
		y=list()
		numels_x_group=int (len(X_Train)/k)

		for i in range (k):
			idx_start=i*numels_x_group

			if (i<k):
				idx_end=idx_start+numels_x_group
				x.append(X_Train[idx_start:idx_end])
				y.append(Y_Train[idx_start:idx_end])
			else:
				x.append(X_Train[idx_start:])
				y.append(Y_Train[idx_start:])

		for i in range (k):
			validation_x=x[i]
			validation_y=y[i]

			new_x_train=self.merge(x,i)
			new_y_train=self.merge (y,i)
			
			obj=LinearRegression ()
			
			obj.fit(new_x_train,new_y_train)

			self.regressors[idx].append(obj)

			pred_train=obj.predict (new_x_train)
			pred_cv=obj.predict (validation_x)

			self.j_train[idx].append(mean_absolute_error(pred_train, new_y_train))
			self.j_cv[idx].append ( mean_absolute_error(pred_cv, validation_y) )
		
	#The merge method recomposes the Training-Set starting from the k-1 folds
	def merge (self,x,jump):

		new_v=list()

		for i in range (len(x)):
			if (i!=jump):
				for j in range(len(x[i])):
					new_v.append(x[i][j])
		return new_v

	#The take_the_best_model_from_last_training method allows you to record ,into the object, some informations about the best Model in your last training
	def take_the_best_model_from_last_training (self):
		best_cv_for_every_model=list()
		self.best_est=list()
		for i in range (len(self.j_cv)):
			self.best_est.append( self.j_cv[i].index( min(self.j_cv[i]) ))
			best_cv_for_every_model.append(min(self.j_cv[i]))

		best_model= best_cv_for_every_model.index(min(best_cv_for_every_model))
		self.index_of_best_model = best_model

		self.error_of_the_best_model= best_cv_for_every_model[best_model]
		self.best_model_features=self.models[best_model]
		self.best_train_for_the_best_model=min (self.j_train[best_model])
		self.best_model=self.regressors[best_model][self.best_est[best_model]]


	#The save_best_estimator method allows you to save into a file the best Model in order to predict data in other programs
	def save_best_estimator (self):

		self.take_the_best_model_from_last_training()

		with open("best_model_features.pkl",'wb') as out:
			pickle.dump({'Best_F':self.best_model_features,},out)

		with open("best_model.pkl",'wb') as out:
			pickle.dump({'Best_M':self.best_model,},out)

	#The plot_graphics method plots the Hypothesis Graphic (2D/3D) for every Model in the last training and the "Degree vs Error " Graphic if it is needed 
	def plot_graphics (self):
		obj=Curve()
		self.take_the_best_model_from_last_training()

		for i in range (len(self.list_of_projected_dataset)):
			obj.plot_2D_H (self.list_of_projected_dataset[i],self.y,self.regressors[i][self.best_est[i]],i+1)
			
		
		for i in range (len(self.models)):
			vb=list(self.list_of_projected_dataset[i])
			vb=list(vb[0])
			if (len(vb)>=2):
				obj.plot_3D_H (self.list_of_projected_dataset[i],self.y,self.regressors[i][self.best_est[i]],i+1)

		if (len(self.rec_deg)>0):
			for i in range (len(self.rec_deg)):
				obj.plot_degree_graphic(self.rec_deg[i].degree,self.rec_deg[i].j_train,self.rec_deg[i].j_cv,self.rec_deg[i].idx)
		
	#The are_equals method allows you to know if 2 models are exactly equal, equal but not for degree or not equal
	def are_equals (self,m_1,m_2):
		for i in range (len(m_1)):
			if (m_1[i]>0 and m_2[i]==0 or m_1[i]==0 and m_2[i]>0):
				return 0 #NOT EQUALS

		if (max(m_1)!=max(m_2)):
			return 1 #EQUALS BUT WITH DIFFERENT DEGREE
		return 2 #EQUALS

	#The take_degree method allows you to know the degree of a model
	def take_degree (self,modello):
		return max(modello)

	#The print_models_errors method allows you to print the Models Erros of the last training 
	def print_models_error (self):
		for i in range (len(self.j_cv)):
			j_t=min(self.j_train[i])
			j_c=min(self.j_cv[i])
			print ("Model Number {} \n    J-Train: {}     J-CV: {} \n".format(i+1,j_t,j_c))
							
			
