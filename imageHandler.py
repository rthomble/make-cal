from wand.image import Image
from wand.font import Font
from wand.color import Color
from wand.drawing import Drawing
import os


#takes an image file, resizes based on inspection and then place onto background then add image overlay and captions


class ImageHandler():
		#define fonts

	def __init__(self,fileNameTuple,outputLocation):
		self.fileName = fileNameTuple[1]
		self.fileDirectory = fileNameTuple[0]
		self.outputDir = outputLocation
		self.sep = os.sep

	def defineFonts(self):
		fontCaption60 = Font(path='./fonts/tyepaloon.ttf',size=20,color=white)
		fontDate85 = Font(path='./fonts/NimbusSanNovDHea.ttf',size=85)
		fontMonth50 = Font(path='./fonts/NimbusSanNovDHea.ttf',size=50)


	def resizeAndOverlayBackground(self,backgroundFile):
		#inspect image for width and height
		with Image(filename=self.fileDirectory+self.sep+self.fileName) as img:
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
		return self.outputDir+self.sep+'rsBG'+self.fileName
