import random
import os
import csv

#checks if it is a holiday. Returns replacement tweet and image file.

class HolidayHandler():
	def __init__(self,holidayListFileName):
		self.fileSep = os.path.sep
		with open(holidayListFileName,'rb') as cf:
			crd = csv.reader(cf,delimiter=",",quotechar='"')
			self.holidays = {row[0]:{'date':row[1],'wday':row[2],'baseDir':row[3],'file':row[4],'text':row[5]} for row in crd}	
		self.checklist = sorted(self.holidays.keys())

	def isHoliday(self,dayOfYear):
		if not (isinstance(dayOfYear,str)):
			dayOfYear = str(dayOfYear)
		if (dayOfYear in self.checklist):
			return True
		else:
			return False
	
	def returnHolidayImageFilenameTuple(self,dayOfYear):
		if not (isinstance(dayOfYear,str)):
			dayOfYear = str(dayOfYear)
		return (self.holidays[dayOfYear]['baseDir'],self.holidays[dayOfYear]['file'])	

	def returnHolidayTweet(self,dayOfYear):
		if not (isinstance(dayOfYear,str)):
			dayOfYear = str(dayOfYear)
		return self.holidays[dayOfYear]['text']	

