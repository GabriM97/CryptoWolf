from Term import Term
from Model import Model
from Cost_Function import Cost_Function
import numpy as np
from Gradient_Descent import Gradient_Descent

#Test Class Term

#TEST 1 - PRINT_E
obj=Term (2)
obj.print_e() #EXPECTED: "Degree: 2"

print ("\n")

#TEST 2 - PRINT_E
obj=Term (3)
obj.print_e() #EXPECTED: "Degree: 3"

print ("\n")

#Test Class Model
obj=Model()

#TEST 1 - ADD_TERM AND PRINT_MODEL
obj.add_term (1)
obj.add_term(1)
obj.add_term(2)
obj.add_term(3)
obj.add_term(1)
obj.print_model () #EXPECTED: "theta_0 + theta_1*x1_elevato_1 + theta_2*x2_elevato2 + theta_3*x3_elevato_3 + theta_4*x4_elevato1

print ("\n")

#TEST 1 - CALC
x=[1,2,7,8,17]
theta=[0.3,2.1,4.3,5.6,2.7]
prediction=obj.calc(x,theta)
prediction=round(prediction,1)
print ("Prediction: {} \n".format (prediction)) #EXPECTED: 3128,3

print ("\n")

#TEST 1 - RESET
obj.reset()
print (len(obj.regressor)) #EXPECTED: 0

print ("\n")

#Test Class Cost_Function
obj=Cost_Function()

#TEST 1 - PERFORM
x=[[1,2,7,8,17],[1,4,5,8,7],[1,5,23,4,9]]
y=[5,8,4]
theta=[0.3,2.1,4.3,5.6,2.7]
n_sample=3
n_param=5
lamb=0.5
model=Model()
model.add_term (1)
model.add_term(1)
model.add_term(2)
model.add_term(3)
model.add_term(1)	
val=obj.perform(model,x,y,n_sample,theta,n_param,lamb)
val=int(val)
print ("Cost: {} \n".format (val)) #EXPECTED: 4303137  

print ("\n")

#TEST 1 - PERFORM_DER_PAR
x=[[1,2,7,8,17],[1,4,5,8,7],[1,5,23,4,9]]
y=[5,8,4]
theta=[0.3,2.1,4.3,5.6,2.7]
n_sample=3
n_param=5
lamb=0.5
model=Model()
model.add_term (1)
model.add_term(1)
model.add_term(2)
model.add_term(3)
model.add_term(1)	
val=obj.perform_der_par(model,x,y,n_sample,theta,n_param,1)
val=int(val)
print ("Derivate: {} \n".format (val)) #EXPECTED: 10514  

print ("\n")

#TEST Class Gradient_Descent
obj=Gradient_Descent()

#TEST 1 - LEARN & GET_TMP_PARAMS
x=[[1,2,7,8,17],[1,4,5,8,7],[1,5,23,4,9]]
y=[5,8,4]
n_sample=3
n_param=5
lamb=0.5
threshold=0.001
alpha=0.00001
model=Model()
model.add_term (1)
model.add_term(1)
model.add_term(2)
model.add_term(3)
model.add_term(1)
theta=obj.learn(model,x,y,n_sample,n_param,lamb,threshold,alpha)
if (type(theta)==int): 
	print ("You have overshooted the minimum, reduce the alpha value \n")
else:
	print ("Tunned Parameters: {} \n".format (theta))

print ("\n")

#TEST 1 - PRINT_ITER_REPORT
obj.print_iter_report()

print ("\n")

#TEST 1 - PLOT_LEARNING_CURVE
obj.plot_learning_curve ()

print ("\n")







