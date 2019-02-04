import pickle
import calendar

#This function transforms a feature scaled value into his original value
def feature_scaling_2_normal (number,feature_scaling_data,target_features):
	return number*feature_scaling_data[0]

#This function is the inverse of the feature_scaling_2_normal function
def normal_2_feature_scaling (candle,feature_scaling_data,target_features):
	new_candle=list()
	counter=0

	for i in range(5):
		if (target_features[i]>0):
			new_candle.append(candle[counter]/feature_scaling_data[i])
	
	return new_candle

#This function transforms a mean normalized value into his original value
def mean_normalization_2_normal (number,mean_normalization_data,target_features): 
	return ((number*mean_normalization_data[0][0])+mean_normalization_data[0][1])

#This function is the inverse of the mean_normalization_2_normal function
def normal_2_mean_normalization (candle,mean_normalization_data,target_features):
	new_candle=list()
	counter=0

	for i in range(5):
		if (target_features[i]>0):
			new_candle.append((candle[counter] - mean_normalization_data[i][1])/mean_normalization_data[i][0])
	
	return new_candle
	
#This function loads a pkl file located into the lib directory.
def load_data (filename):
	path="./lib/"
	filename=path+filename
	try:
		with open (filename,"rb") as inp:
			data=pickle.load(inp)
	except IOError:
		return -1
	return data

#This function checks if a specific pkl file ,located into the lib directory, is present
def check_file (filename):
	path="./lib/"
	filename=path+filename
	try:
		with open (filename,"rb") as inp:
			return 7
	except IOError:
		return -1

#This function checks the correctness of a datetime
def check_date_time (day,month,year,hour,minutes):
	leap=0

	if (year<2):
		return -1

	if (month<1 or month>12):
		return -2

	if (hour>23 or hour<0):
		return -3

	if (minutes>59 or minutes<0):
		return -4

	if (calendar.isleap(year)):
		leap=1

	if (month==2):
		if (leap==1):
			if (day<1 or day>29):
				return -5
		else:
			if (day<1 or day>28):
				return -6

	elif (month!=4 and month!=6 and month!=9 and month!=11):
		if (day<1 or day>31):
			return -7
	else:
		if (day<1 or day>30):
			return -8
	return 0

def check_format (data):

	if (type(data)!=int):
		print ("Error, you have to insert a number \n")
		return -1

	return 0		
			

