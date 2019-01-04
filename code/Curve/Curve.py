"""

Curve class helps you to plot some useful Graphics for Learning phase monitoring

"""

from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

class Curve:

	#The "plot_2D_H" method plots 2D-Hypothesis Graphic for the first feature of the Training-Set
	def plot_2D_H (self,x_list,y_list,regressor):

		plt.figure()
		plt.plot(x_list,y_list,'x')

		theta = regressor.coef_
		theta_0=regressor.intercept_
		theta_1=theta [0]

		#x=np.arange(-0.6,0.8,0.1)
		x=np.arange(min(x_list),max(x_list),0.1)

		plt.plot(x,theta_0+x*theta_1,'r')

		plt.title('2D-Hypothesis Plot')
		plt.xlabel('Feature-1') 
		plt.ylabel('Right-Value')
		plt.show()

	#The "plot_3D_H" method plots 3D-Hypothesis Graphic for the first two features of the Training-Set
	def plot_3D_H (self,x_list,y_list,z_list,regressor):
		
		fig = plt.figure()
		v=plt.subplot(111, projection='3d')
		
		theta = regressor.coef_
		theta_0=regressor.intercept_
		theta_1=theta [0]
		theta_2=theta[1]

		#x_range= np.arange(-1,1,0.1)
		#y_range= np.arange(-1,1,0.1)
		x_range= np.arange(min(x_list),max(x_list),0.1)
		y_range= np.arange(min(y_list),max(y_list),0.1)

		x,y=np.meshgrid(x_range,y_range)

		plt.plot(x_list,y_list,z_list,'x')

		plt.gca().plot_surface(x,y,theta_0+theta_1*x+theta_2*y,shade=False,color='r')

		plt.title('3D-Hypothesis Plot')
		plt.xlabel('Feature-1') 
		plt.ylabel('Feature-2')
		v.set_zlabel('Right-Value')

		plt.show()

	#The "plot_degree_graphic" method plots the "Degree vs Error" Graphic
	def plot_degree_graphic (self,degree,j_train,j_cv):
		plt.figure() 
		plt.plot(degree,j_train)
		plt.plot(degree,j_cv) 

		plt.title('Degree vs Error Graphic')
		plt.xlabel('degree') 
		plt.ylabel('error') 

		plt.legend(['J-Train','J-CV']) 
		plt.show()

	
