class Model_Printer:

	def print_input_models (self,models):

		if (len(models)==0):
			print ("Error, You have passed an empty list :( \n")
			return;

		empty_model=list()
		for i in range (len(models[0])):
			empty_model.append(0)

		for j in range (len(models)):
			if (models[j]!=empty_model):
				print ("Model Number {} \n".format (j+1))
				print ("h_theta_(x)= theta_0 + ")

				k=1

				for i in range (len (models[j])):
					if (models[j][i]>0):
						print ("theta_{}*x{}_exp_{} + ".format(k,i+1,models[j][i]))
						k=k+1

				print ("")
