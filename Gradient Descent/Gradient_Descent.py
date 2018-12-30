"""
This object rappresents a tool that perform the Gradient Descent Algorithm  

"""
import numpy as np
from Cost_Function import Cost_Function 
from matplotlib import pyplot as plt

class Gradient_Descent:

	#The learn method allows you to learn the parameters that minimize the Cost Function
	def learn (self,model,x,y,n_ele,n_param,lamb,threshold,alpha):
		self.db=list()
		self.iter=list()

		param=np.random.rand (n_param)
		tmp_params=np.random.rand (n_param)

		err=0
		cost=Cost_Function()
		j_act=round(cost.perform (model,x,y,n_ele,param,n_param,lamb),3)
		j_prec=j_act
		self.db.append(j_act)
		self.iter.append(1)

		cont=1

		while True:

			cont+=1
	
			tmp_params=self.get_tmp_params (param,tmp_params,n_param,alpha,lamb,n_ele,model,x,y)
			param=tmp_params

			j_prec=j_act
			j_act=round(cost.perform (model,x,y,n_ele,param,n_param,lamb),3)
			self.db.append(j_act)
			self.iter.append(cont)

			if (j_act>j_prec):
				err=1
				break

			if ((j_prec-j_act)<=threshold):
				break
		
		if (err==1):
			return (-5)	
		
		return param

	#The get_tmp_params method allows you to perform the "Simultanius Update" of the theta parameters
	def get_tmp_params (self,param,tmp_params,n_param,alpha,lamb,n_ele,model,x,y):
		cost=Cost_Function()

		for i in range (n_param):

			if (i==0):
				tmp_params[i]=param[i]-alpha*cost.perform_der_par (model,x,y,n_ele,param,n_param,i)		
			else:
				tmp_params[i]=((param[i]*(1-((alpha*lamb)/n_ele))) - (alpha * cost.perform_der_par (model,x,y,n_ele,param,n_param,i)))

		return tmp_params

	#The plot_learning_curve method allows you to plot the (Number_of_Iterations VS Error) Graphic
	def plot_learning_curve (self):
		plt.plot(self.iter,self.db)
        
		plt.xlabel('Iterations')
		plt.ylabel('Error')   
		plt.title('Learning Curve') 
		plt.show() 

	#The print_iter_report method allows you to visualize a report of last Gradient Descent Execution, for every iteration you can view the Cost Function Value
	def print_iter_report (self):
		for i in range(len(self.iter)):
			print ("Iter: {} - J: {} \n".format (self.iter[i],self.db[i]))



