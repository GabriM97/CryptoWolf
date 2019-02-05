"""

Curve class helps you to plot some useful Graphics for Learning phase monitoring

"""

from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

class Curve:

	#The "plot_2D_H" method plots 2D-Hypothesis Graphic for the first feature of the Training-Set
	def plot_2D_H (self,x_list,y_list,regressor,model):

		x_1=list()
		for i in range (len(x_list)):
			x_1.append(x_list[i][0])

		if (x_1[0]>=100000):
			return -1

		plt.figure()
		plt.plot(x_1,y_list,'x')

		theta = regressor.coef_
		theta_0=regressor.intercept_
		theta_1=theta [0]

		
		#x=np.arange(0.0, 5000, 100.0)	
		x=np.arange(min(x_1),max(x_1),0.1)

		plt.plot(x,theta_0+x*theta_1,'r')

		plt.title('Model {} - 2D-Hypothesis Plot'.format(model))
		plt.xlabel('Feature-1') 
		plt.ylabel('Price in Dollar')
		plt.show()

	#The "plot_3D_H" method plots 3D-Hypothesis Graphic for the first two features of the Training-Set
	def plot_3D_H (self,x_list,z_list,regressor,model):
		x_1=list()
		for i in range (len(x_list)):
			x_1.append(x_list[i][0])

		x_2=list()
		for i in range (len(x_list)):
			x_2.append(x_list[i][1])

		if (x_1[0]>=100000):
			return -1

		if (x_2[0]>=100000):
			return -1

		fig = plt.figure()
		v=plt.subplot(111, projection='3d')
		
		theta = regressor.coef_
		theta_0=regressor.intercept_
		theta_1=theta [0]
		theta_2=theta[1]

		#x_range=np.arange(0.0, 5000, 100.0)
		#y_range=np.arange(0.0, 5000, 100.0)

		x_range= np.arange(min(x_1),max(x_1),2.0)
		y_range= np.arange(min(x_2),max(x_2),2.0)

		x,y=np.meshgrid(x_range,y_range)

		plt.plot(x_1,x_2,z_list,'x')

		plt.gca().plot_surface(x,y,theta_0+theta_1*x+theta_2*y,shade=False,color='r')

		plt.title('Model {} - 3D-Hypothesis Plot'.format(model))
		plt.xlabel('Feature-1') 
		plt.ylabel('Feature-2')
		v.set_zlabel('Price in Dollar')

		plt.show()

	#The "plot_degree_graphic" method plots the "Degree vs Error" Graphic
	def plot_degree_graphic (self,degree,j_train,j_cv,idx):
		plt.figure() 
		plt.plot(degree,j_train)
		plt.plot(degree,j_cv)
		mi=min(idx)+1
		ma=max(idx)+1 
		plt.title('Models {}-{} Degree vs Error Graphic'.format(mi,ma))
		plt.xlabel('degree') 
		plt.ylabel('error') 

		plt.legend(['J-Train','J-CV']) 
		plt.show()

	
