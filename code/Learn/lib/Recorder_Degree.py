"""

This class helps you to build the "Degree vs Error" Graphic

"""
class Recorder_Degree:

	#The constructor initializes 4 lists that will contain the values of degree,  j_train, j_cv  respectively and index values
	def __init__ (self):
		self.degree=list()
		self.j_train=list()
		self.j_cv=list()
		self.idx=list()

	#The record method puts new values into the fourlists
	def record (self,degree,j_train,j_cv,idx):
		self.degree.append(degree)
		self.j_train.append(j_train)
		self.j_cv.append(j_cv)
		self.idx.append(idx)
