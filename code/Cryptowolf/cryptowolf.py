import sys  
sys.path.append('./lib')  
from Cleaner import Cleaner
import time
from cryptowolf_assets import *
from Time_Stamp_Converter import Time_Stamp_Converter
from Extractor import Extractor

pca_v=False

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
	pca=pca['pca']
	pca_v=True


#Here, we extract the daily opened candle, in order to predict the ClosePrice
e = Extractor()
daily_not_closed_candle = e.ohlc ("bitstamp","btcusd",-5,"1549152000","43200")

if (type(daily_not_closed_candle)==int and x==-1): 
	print ("Bad Request - Unable to download last candlestick from the internet\n")


elif (type(daily_not_closed_candle)==int and x==-2):
	print ("You have finished your CPU allowance, retry next hour - Unable to download last candlestick from the internet\n")


elif (type(daily_not_closed_candle)==int and x==-3):
	print ("Unexpected Error - Unable to download last candlestick from the internet\n")


else:

	pr=list()
	pr.append( daily_not_closed_candle['result'] ['43200'] [-1] )
	del (pr[0][4]) #We delete the temporary candle ClosePrice
	del (pr[0][5]) #We delete the last feature because it isn't documented in the CryptoWatch API
	print ("\n\n*******************CRYPTOWOLF-DAILY-CANDLE-PREDICTION*******************\n")
	print ("Daily Opened Candle: \n\n {} \n".format(pr[0]))

	daily_prediction=list()
	pr=pr[0]

	#If was applied normalization in the learning phase we need to apply it as well in the input query
	if (normalization_level==1):
		candle=normal_2_feature_scaling(pr,pack,target_features)

	if (normalization_level==2):
		candle=normal_2_mean_normalization(pr,pack,target_features)

	daily_prediction.append(pr)
		
	#If learning was done using pca technique, we apply pca as well in the input query
	if (pca_v==True):
		daily_prediction=pca.transform(daily_prediction)

	#Here we make the prediction
	daily_prediction=estimator.predict(daily_prediction)

	#If we perform some trasformation on the input query, we need to return back in order to show a coherent result to the user
	if (normalization_level==1):
		daily_prediction=feature_scaling_2_normal (daily_prediction,pack,target_features)

	if (normalization_level==2):
		daily_prediction=mean_normalization_2_normal (daily_prediction,pack,target_features)
	
	print ("The Predicted ClosePrice is {} \n".format(float(daily_prediction)))
 



#Here is the core of the program, infact in this point we ask to insert a candle in order to predict her ClosePrice
while (True):
	
	print ("\n\n*******************CRYPTOWOLF-PREDICT-FROM-INPUT*******************\n")
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
				print ("Choose a CloseTime input format type, type \n 0 -> Date and Time \n 1 -> Timestamp\n")
				choose=int(input("\n -> "))

				if (choose==1):
					print ("Insert a CloseTime Value, which must be a UNIX timestamp")
					closeP=float(input ("\n -> "))

					candle.append(closeP)
					print("")
				else:
					print ("\nInsert a Day")
					day=int(input("\n -> "))

					print ("\nInsert a Month")
					month=int(input("\n -> "))

					print ("\nInsert an Year")
					year=int(input("\n -> "))

					print ("\nInsert an hour")
					hour=int(input("\n -> "))

					print ("\nInsert the minutes")
					minutes=int(input("\n -> "))
					print("")

					risult = check_date_time (day,month,year,hour,minutes)
					if (risult==0):
						tp = Time_Stamp_Converter ()
						closeT=tp.convert (day,month,year,hour,minutes)
						closeT= float(closeT)
						print ("You have inserted the fallowing Date and Time: {}-{}-{} {}:{} \n".format(day,month,year,hour,minutes)) 
						print ("The corrisponding UNIX Timestamp is {} \n".format(int(closeT)))
						candle.append(closeT)
						print("")
					else:
						print ("\nError, you have inserted a wrong date and time, please retry\n")
						continue	


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
			
			#If learning was done using pca technique, we apply pca as well in the input query
			if (pca_v==True):
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
	except ValueError:
		print ("\nError, you have to insert a numeric value \n")


#End of program
print ("Closing the Program, Bye.....")
time.sleep(0.7)
	



