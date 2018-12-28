"""
This class convert an UTC date-time into a UNIX Timestamp. The time is per default 00:00:00

"""

from datetime import datetime, date
import calendar

class Time_Stamp_Converter:

	#The convert method converts a date into a timestamp, you have to pass day,month and year to the function. Time is ,per default, setted to 00:00:00
	def convert (self,day,month,year):
		d = date(year, month, day)
		self.timestamp = calendar.timegm(d.timetuple())
		return self.timestamp
	#The print_last_timestamp method prints the last timestamp in a date-time format
	def print_last_timestamp (self):
		print(datetime.utcfromtimestamp(self.timestamp))
