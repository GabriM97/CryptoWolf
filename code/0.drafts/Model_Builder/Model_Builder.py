"""

The Model_Builder class helps you to build a well-done list of Models, in a interactive way

"""

import numpy as np
import copy
import pickle

class Model_Builder:

	#The costructor inizializes the 'setted' attribute
	def __init__ (self):
		self.setted=0

	#The build method builds a set of Models in a interactive way
	def build (self,X_Train):

		n=len(X_Train[0])
		print ("Max Features Number: {}".format(n))
		print ("")

		try:
    			n_models=int(input('How many models do you want to build? \n'))
		except ValueError:
    			print ("Not a number")

		if (n_models<=0):
			print ("Bad Answer Format, retry \n")
			return

		print ("")
		print ("Will be created {} Models".format(n_models))
		print ("")

		self.models=list()
		sample_model=list()

		for i in list(range(n)):
			sample_model.append(-1)

		for i in list(range(n_models)):
			self.models.append(copy.deepcopy(sample_model))

		for i in list(range (n_models)):
			print ("Model Number {} \n".format(i+1))
			print ("")

			for j in list(range (n)):

				try:
    					choose=input("Do you want to put in the feature number {} ? \n Please, answer 'yes' or 'no' \n".format(j+1))
				except ValueError:
    					print ("Not a number")

				print ("")
				if (type(choose)!=str):
					print ("Bad Answer Format, retry")
					return

				if (type(choose)==str and 'yes'!=choose and 'no'!=choose):
					print ("Bad Answer Format, retry")
					return

				if (choose=='yes'):
					print ("You have inserted the feature Number {} !".format(j+1))
					print ("")

					try:
    						degree=int(input('What degree do you want to assign to the feature Number {}? \n Please type a number between 1 to infinity \n'.format(j+1)))
					except ValueError:
    						print ("Not a number")

					print ("")
					if (degree<=0):
						print ("Error, you have inserted a non-valid degree, retry \n")
						return

					print ("You have assigned Degree {} to the feature Number {} ".format(degree,j+1))
					print ("")
					self.models[i][j]=degree
					self.setted=1
				else:
					print ("You have removed the feature Number {} !".format(j+1))
					print ("")
					self.models[i][j]=0

		self.print_last_list()
		return self.models

	#The print_last_list method prints the last set of Models built
	def print_last_list (self):

		if (self.setted==0):
			print ("Error, there isn't any model in the list :( \n")
			return;

		empty_model=list()
		for i in range (len(self.models[0])):
			empty_model.append(0)

		for j in range (len(self.models)):
			if (self.models[j]!=empty_model):
				print ("Model Number {} \n".format (j))
				print ("h_theta_(x)= theta_0 + ")

				k=1

				for i in range (len (self.models[j])):
					if (self.models[j][i]>0):
						print ("theta_{}*x{}_exp_{} + ".format(k,i+1,self.models[j][i]))
						k=k+1

				print ("")

	def print_input_models (self,models):

		if (len(models)==0):
			print ("Error, You have passed an empty list :( \n")
			return;

		empty_model=list()
		for i in range (len(models[0])):
			empty_model.append(0)

		for j in range (len(models)):
			if (models[j]!=empty_model):
				print ("Model Number {} \n".format (j+1))
				print ("h_theta_(x)= theta_0 + ")

				k=1

				for i in range (len (models[j])):
					if (models[j][i]>0):
						print ("theta_{}*x{}_exp_{} + ".format(k,i+1,models[j][i]))
						k=k+1

				print ("")

	#The save_models method saves the last set of Models built in a .pkl file
	def save_models (self):

		if (self.setted>0):
			with open("models.pkl",'wb') as out:
				pickle.dump({'Models':self.models,},out)
		else:
			print ("Error, there isn't any model in the list :( \n")

	#The load_models method loads from a .pkl file the last set of Models built
	def load_models (self):
		try:
			with open("models.pkl", "rb") as inp:
				data=pickle.load(inp)
		except IOError:
			return -1
		return data
