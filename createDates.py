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
	mon = calendar.month_abbr[i+1]
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
					t = next(tweetList)
					img = imageHandler.ImageHandler(outputDir)

					print calendar.day_name[wkday]+" "+ mon + " " + str(date)
					print "Opening: " + fileTuple[1]

					img.setImage(fileTuple)
					resizeTuple = img.resizeAndOverlayBackground(backgroundImg)
					print "Created: " resizeTuple[1]

					#OPTIMIZE: remove ^ by just passing image along to next step
					img.setImage(resizeTuple)
					finalTuple = img.addDateAndText(t,date,calendar.day_abbr[wkday],mon)
					print "Created: " finalTuple[1]
			elif wkday == 5:
				#saturday
				pass
			else:
				#sunday
				pass


