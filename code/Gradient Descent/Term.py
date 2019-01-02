"""
This object rappresents a single term of the Hypothesis Function. (i.e. A term is "theta_1 * x_1_exp_2")  

"""
import numpy as np
class Term:
	
	#The Costructor inizializes the degree of the Hypothesis term enclosed into the object
	def __init__ (self,degree):
		self.degree=degree

	#The print_e method prints the degree of the term enclosed into the object 
	def print_e (self):
		print ("Degree: {} ".format (self.degree))		
