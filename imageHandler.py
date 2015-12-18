from wand.image import Image
from wand.font import Font
from wand.color import Color
from wand.drawing import Drawing
import os


#takes an image file, resizes based on inspection and then place onto background then add image overlay and captions


class ImageHandler():
		#define fonts

	def __init__(self,outputLocation):
		self.outputDir = outputLocation
		self.sep = os.sep
		self.fontTweet20 = Font(path='./fonts/tyepaloon.ttf',size=20)
		self.fontMonth60 = Font(path='./fonts/tyepaloon.ttf',size=60)

	def setImage(self,fileNameTuple):
		self.fileName = fileNameTuple[1]
		self.fileDirectory = fileNameTuple[0]
		self.currentImageFilePath = self.fileDirectory + self.sep + self.fileName

	def resizeAndOverlayBackground(self,backgroundFile):
		#inspect image for width and height
		with Image(filename=self.currentImageFilePath) as img:
			sz = img.size
			if (sz[0] >= sz[1]):	
				img.sample(1115,835)
			else:
				img.sample(835,1115)
			if img.width > img.height:
				img.rotate(90)
			with Image(filename=backgroundFile) as bg_img:
				bg_img.composite(img,top=5,left=285)

				bg_img.save(filename=self.outputDir+self.sep+'rsBG'+self.fileName)
			return (self.outputDir,'rsBG'+self.fileName)

	def addDateAndText(self,tweet,day,weekday,month):
		#MUST CALL setImage fist
		with Image(filename=self.currentImageFilePath) as img:
			#create day of week
			img.caption(weekday,left=90,top=65,width=108,height=56,font=font,gravity='north_west')

			#create date of month
			img.caption('%02d' % (day),left=116,top=116,width=72,height=56,font=font,gravity='north_west')

			#create month 
			img.caption(month,left=90,top=172,width=108,height=56,font=font,gravity='north_west')

			#create tweet 
			img.caption(t,left=25,top=350,width=260,height=500,font=font20,gravity='north_west')
		
			img.save(filename=self.outputDir+self.sep+ weekday + mon + day + "page.jpg")	
		return (self.outputDir, weekday + mon + day + "page.jpg")	
			
