import sys
import tweetHandler
import calendar 
import fileNameHandler
import imageHandler

backgroundImg = "/Users/rthomble/Documents/Programming/cal/fullBack.jpg"
outputDir = "/Users/rthomble/Documents/Programming/cal/dPhoto/testing"
c = calendar.Calendar()
yearDates = c.yeardays2calendar(2016,12)

tweetObj = tweetHandler.TweetHandler("/Users/rthomble/Documents/Programming/cal/tweets.txt",23,60)
tweetList = tweetObj.getTweetText()

vertFiles = fileNameHandler.FileNameHandler("/Users/rthomble/Documents/Programming/cal/dPhoto/vertical")
fileList = vertFiles.returnRandomFile()

for i,month in enumerate(yearDates[0]):
	mon = calendar.month_name[i+1]
	for week in month:
		for (date,wkday) in week:
			if (date > 9):
				sys.exit()
			if wkday < 5:
				#weekday
				if date == 0:
					pass
				else:
					fileTuple = next(fileList)
					img = imageHandler.ImageHandler(fileTuple,outputDir)
					print img.resizeAndOverlayBackground(backgroundImg)
					print calendar.day_name[wkday]+" "+ mon + " " + str(date)
					print next(tweetList)
					print fileTuple[1]
			elif wkday == 5:
				#saturday
				pass
			else:
				#sunday
				pass


