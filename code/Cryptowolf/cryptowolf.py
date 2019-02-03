import sys  
sys.path.append('./lib')  
from Cleaner import Cleaner
import time
from cryptowolf_assets import *

#We used ,here, the Cleaner class in order to load the normalization data
obj = Cleaner ("bitstamp","btcusd","12-h")



#Here we load the estimator features
target_features = load_data("best_model_features.pkl")

if (target_features == -1):
	print ("Fatal Error, missing some data file \n")
	exit(4)

target_features=target_features['Best_F']


#Here we load the estimator Object
estimator = load_data("best_model.pkl")

if (estimator == -1):
	print ("Fatal Error, missing some data file \n")
	exit(5)

estimator=estimator['Best_M']



#This variable signals what is the Normalization Level (None, Feature_Scaling, Mean Normalization)
normalization_level=0



#Here we try to load feature scaling information
result=check_file("43200_feature_scaling_max.plk")
if (result==7):
	normalization_level=1
	pack = obj.open_feature_scaling_max()



#Here we try to load mean normalization information (of course feature scaling excludes mean normalization and vice versa)
result=check_file("43200_mean_norm_info.plk")
if (result==7):
	normalization_level=2
	pack = obj.open_mean_norm_info()



#Here we load the pca object
result=check_file("pca.plk")
if (result==7):
	pca = load_data("pca.plk")

	if (pca==-1):
		print ("Fatal Error, missing some data file \n")
		exit(4)	

	pca=pca['pca']



#Here is the core of the program, infact in this point we ask to insert a candle in order to predict her ClosePrice
while (True):
	
	print ("\n\n*******************CRYPTOWOLF*******************")
	print ("1) Predict a ClosePrice starting from a candle")
	print ("2) Exit")
	
	try:

		choose=int(input ("\n -> "))
		print("")

		#Number inserted must be between 1 or 2
		if (choose>2 or choose<1):
			print ("Error, you have to insert a number between 1 and 2 \n")
			continue

		#Here start the dialog with the user in order to make the prediction
		if (choose==1):

			candle=list()

			#In the fallowing code lines, we ask to the user only the features that accept the estimator			

			if (target_features[0]>0):
				print ("Insert a CloseTime Value, which is a UNIX timestamp")
				closeP=float(input ("\n -> "))
				candle.append(closeP)
				print("")


			if (target_features[1]>0):
				print ("Insert a OpenPrice Value")
				openP=float(input ("\n -> "))
				candle.append(openP)
				print("")


			if (target_features[2]>0):
				print ("Insert a HighPrice Value")
				highP=float(input ("\n -> "))
				candle.append(highP)
				print("")


			if (target_features[3]>0):
				print ("Insert a LowPrice Value")
				lowP=float(input ("\n -> "))
				candle.append(lowP)
				print("")


			if (target_features[4]>0):
				print ("Insert a Volume Value")
				volume=float(input ("\n -> "))
				candle.append(volume)
				print("")


			print ("Candle Inserted ---> {} ".format(candle))


			input_prediction=list()

			
			#If was applied normalization in the learning phase we need to apply it as well in the input query
			if (normalization_level==1):
				candle=normal_2_feature_scaling(candle,pack,target_features)

			if (normalization_level==2):
				candle=normal_2_mean_normalization(candle,pack,target_features)


			input_prediction.append(candle)

			#The learning was done using pca technique, for this reasing we apply pca as well in the input query
			input_prediction=pca.transform(input_prediction)

			#Here we make the prediction
			prediction=estimator.predict(input_prediction)

			#If we perform some trasformation on the input query, we need to return back in order to show a coherent result to the user
			if (normalization_level==1):
				prediction=feature_scaling_2_normal (prediction,pack,target_features)

			if (normalization_level==2):
				prediction=mean_normalization_2_normal (prediction,pack,target_features)


			print ("\n\nThe predicted ClosePrice is {} ".format(float(prediction))) 
		
		#Case Exit	
		elif (choose==2):
			break
		
	#Case of bad input, the program expects a numeric value		
	except ValueError:
		print ("Error, you have to insert a number \n")



#End of program
print ("Closing the Program, Bye.....")
time.sleep(0.7)
	



