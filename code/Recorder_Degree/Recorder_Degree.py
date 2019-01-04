"""

This class helps you to build the "Degree vs Error" Graphic

"""
class Recorder_Degree:

	#The constructor initializes 3 lists that will contain the values of degree,  j_train and j_cv  respectively.
	def __init__ (self):
		self.degree=list()
		self.j_train=list()
		self.j_cv=list()

	#The record method puts new values into the three lists
	def record (self,degree,j_train,j_cv):
		self.degree.append(degree)
		self.j_train.append(j_train)
		self.j_cv.append(j_cv)
