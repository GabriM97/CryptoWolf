"""
This object rappresents a specific Hypothesis Function, this Hypothesis may be changed at run-time 

"""

from Term import Term
import numpy as np

class Model:

	#Costructor inizializes the regressor list, the regressor list is a dynamic list of Hypothesis Terms 
	def __init__ (self):
		self.regressor=list()
	
	#The add_term method allows you to add a term in your Hypothesis
	def add_term (self,degree):
		term=Term(degree)	
		self.regressor.append (term)

	#The reset method allows you to reset the regressor list in order to build a brand new model
	def reset (self):
		self.regressor=list()

	#The Calc method allows you to calculate the Hypothesis, of course you have to pass ,into the call-function, the sample-vector and the theta-vector
	def calc (self,x,param):
		if (len(self.regressor)<=1):
			print ("Error, model isn't setted \n")
			return;

		if ((len(x))!=len(param) or len (param) != (len(self.regressor))):
			print ("Error, the passed datas are incoerent with the model")
			return
		
		prediction=0.0
		prediction+=param[0]
		for i in range (1,len(self.regressor)):
			prediction+=(x[i]**self.regressor[i].degree)*param[i]	
		return prediction

	#The print_model method allows you to visualize the Model that you have built, in order to understand the scenary
	def print_model (self):
		if (len(self.regressor)<=1):
			print ("Error, model isn't setted \n")
			return;

		print ("h_theta_(x)= theta_0 + ")

		for i in range (1,len (self.regressor)):
			print ("theta_{}*x{}_exp_{} + ".format(i,i,self.regressor[i].degree))
		


