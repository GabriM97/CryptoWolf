"""
This object rappresents a "Cost Function" facility. 
Thanks this object, you can automate the Cost Function Calculation and the Cost Function Derivate Calculation

"""

from Model import Model

class Cost_Function:

	#The perform method calculates the Cost Function
	def perform (self,model,x,y,n_element,param,n_param,lamb):
		square_err=0.0
		par_sum=0.0
		for i in range (n_element):
			val=model.calc(x[i],param)
			square_err+=(val-y[i])**2
		for i in range (n_param):
			par_sum+=(param[i])**2
		par_sum=par_sum*lamb
		numeratore=par_sum+square_err
		ris=numeratore/(2*n_element)
		return ris

	#The perform_der_par method calculates the Derviate of Cost Function
	def perform_der_par (self,model,x,y,n_element,param,n_param,term_r_der):
		square_err=0.0
		for i in range (n_element):
			val=model.calc(x[i],param)
			val=(val-y[i])*x[i][term_r_der]
			square_err+=val
		ris=square_err/(n_element)
		return ris	
		

