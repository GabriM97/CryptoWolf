"""

The Dataset_Projector class helps you to perform a projection in a Dataset

"""

class Dataset_Projector:

	#The to_project method helps you to perform a projection in a Dataset passed in input
	def to_project (self,X_Train,list_of_projected_features):
		Projected_X_Train=list()

		for i in range(len(X_Train)):
			Projected_X_Train.append(-1)
		
		for i in range(len(X_Train)):
			Projected_X_Train[i]=list()

			for j in range (len(X_Train[0])):
				if (list_of_projected_features[j]>0):
					if (list_of_projected_features[j]==1):
						Projected_X_Train[i].append(X_Train[i][j])
					else:
						Projected_X_Train[i].append( X_Train[i][j]**list_of_projected_features[j] )
		
		return Projected_X_Train
				



					
						
		

	
