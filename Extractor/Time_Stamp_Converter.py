"""
This class convert an UTC date-time into a UNIX Timestamp.

"""

from datetime import datetime 
import pytz

class Time_Stamp_Converter:

	#The convert method converts a date-time into a timestamp, you have to pass day, month, year, hour and minutes to the function.
	def convert (self,day,month,year,hour,minutes):
		obj=datetime (year, month, day, hour, minutes)
		self.timestamp=obj.timestamp()
		return self.timestamp

	#The print_last_timestamp method prints the last timestamp in a date-time format
	def print_last_timestamp (self):
		utc_dt = datetime.utcfromtimestamp(self.timestamp).replace(tzinfo=pytz.utc) 
		print(utc_dt.strftime("%d-%m-%Y %H:%M"))
