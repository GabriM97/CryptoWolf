"""
This class converts date and time ,expressed in local timezone, into a UNIX Timestamp.

"""

from datetime import datetime 
import pytz

class Time_Stamp_Converter:

	#The convert method converts date and time ,expressed in local timezone, into a timestamp.                                              
	#You have to pass day, month, year, hour and minutes to the function.
	def convert (self,day,month,year,hour,minutes):
		obj=datetime (year, month, day, hour, minutes)
		self.timestamp=obj.timestamp()
		ret=str(self.timestamp)
		ret=ret[:len(ret)-2]
		return ret

	#The get_date method take in input an integer that rappresents a timestamp, and returns a string that rappresents the corresponding date-time in local timezone
	def get_date (self,timestamp):
		sw=datetime.fromtimestamp(timestamp)
		sw=sw.strftime("%d-%m-%Y %H:%M")
		return sw

	

