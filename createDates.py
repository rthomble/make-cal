import sys
import tweetHandler
import calendar 
import fileNameHandler
import imageHandler
import holidayHandler
import time

backgroundImg_vert = "/Users/rthomble/Documents/Programming/cal/finalBack_vert.jpg"
backgroundImg_horiz = "/Users/rthomble/Documents/Programming/cal/finalBack_horiz.jpg"
backgroundImg_square = "/Users/rthomble/Documents/Programming/cal/finalBack_square.jpg"

outputDir_rsBG = "/Users/rthomble/Documents/Programming/cal/dPhoto/testing/rsBG"
outputDir_final = "/Users/rthomble/Documents/Programming/cal/dPhoto/testing"

tweetObj = tweetHandler.TweetHandler("/Users/rthomble/Documents/Programming/cal/tweets.txt",23,60)
tweetList = tweetObj.getTweetText()

holidays = holidayHandler.HolidayHandler("/Users/rthomble/Documents/Programming/cal/holidays.csv")

vertFiles = fileNameHandler.FileNameHandler("/Users/rthomble/Documents/Programming/cal/dPhoto/vert")
v_fileList = vertFiles.returnRandomFile()
#could add a separate folder just for the holiday photos.  May not need to do that right now

horizFiles = fileNameHandler.FileNameHandler("/Users/rthomble/Documents/Programming/cal/dPhoto/horiz")
h_fileList = horizFiles.returnRandomFile()

squareFiles = fileNameHandler.FileNameHandler("/Users/rthomble/Documents/Programming/cal/dPhoto/square")
s_fileList = squareFiles.returnRandomFile()

for yrDay in range(1,367):
	t = time.strptime(str(yrDay) + ' 2016','%j %Y')
	mon,wkday,mday = calendar.month_abbr[t.tm_mon],calendar.day_abbr[t.tm_wday],t.tm_mday
	if t.tm_wday < 5:
		page_type,backgroundImg,fileList = 'vert',backgroundImg_vert,v_fileList
	elif t.tm_wday == 5:
		page_type,backgroundImg,fileList = 'horiz',backgroundImg_horiz,h_fileList
	elif t.tm_wday == 6:
		page_type,backgroundImg,fileList = 'square',backgroundImg_square,s_fileList

	if holidays.isHoliday(yrDay):
		fileTuple = holidays.returnHolidayImageFilenameTuple(yrDay)
		twt = holidays.returnHolidayTweet(yrDay)
	else:
		fileTuple = next(fileList)
		twt = next(tweetList)

	img = imageHandler.ImageHandler(page_type)

	#print calendar.day_name[wkday]+" "+ mon + " " + str(date)
	#print "Opening: " + fileTuple[1]

	img.setImage(fileTuple,outputDir_rsBG)
	resizeTuple = img.resizeAndOverlayBackground(backgroundImg)
	#print "Created: "+ resizeTuple[1]

	#OPTIMIZE: remove ^ by just passing image along to next step

	img.setImage(resizeTuple,outputDir_final)
	finalTuple = img.addDateAndText(twt,mday,wkday,mon)
	print "Created: "+ finalTuple[1]

	if yrDay > 5:
		sys.exit()

