import random
import os
import csv

#checks if it is a holiday. Returns replacement tweet and image file.

class HolidayHandler():
	def __init__(self,holidayListFileName):
		self.fileSep = os.path.sep
		with open(holidayListFileName,'rb') as cf:
			crd = csv.reader(cf,delimiter=",",quotechar='"')
			self.holidays = {row[0]:{'date':row[1],'wday':row[2],'file':row[3],'text':row[4]} for row in crd}	
		self.checklist = sorted(self.holidays.keys())

	def isHoliday(self,dayOfYear):
		if not (isinstance(dayOfYear,str)):
			dayOfYear = str(dayOfYear)
		if (dayOfYear in self.checklist):
			return True
		else:
			return False

	def returnHolidayImageFileName(self,dayOfYear):
		if not (isinstance(dayOfYear,str)):
			dayOfYear = str(dayOfYear)
		return self.holidays[dayOfYear]['file']	

	def returnHolidayTweet(self,dayOfYear):
		if not (isinstance(dayOfYear,str)):
			dayOfYear = str(dayOfYear)
		return self.holidays[dayOfYear]['text']	


def testHolidays():
	h = HolidayHandler("/Users/rthomble/Documents/Programming/cal/codeFinal/horizHolidays.csv")
	assert h.isHoliday(184)
	assert h.returnHolidayImageFileName(184) == 'horiz_dog - 49.jpg'
	assert h.isHoliday(331)
	assert h.returnHolidayImageFileName(331) == 'horiz_dog - 48.jpg'
	assert h.isHoliday(359)
	assert h.returnHolidayImageFileName('359') == 'horiz_dog - 10.jpg'
	assert h.isHoliday(366)
	assert not h.isHoliday(22)
	assert not h.isHoliday(3.22)
	print "looks good"


#testHolidays()

