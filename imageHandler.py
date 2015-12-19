from wand.image import Image
from wand.font import Font
from wand.color import Color
from wand.drawing import Drawing
import os


#takes an image file, resizes based on inspection and then place onto background then add image overlay and captions


class ImageHandler():
	#width,height
	typeSize = {'square':(1115,1115),'horiz':(1115,835),'vert':(835,1115)}

	def __init__(self,outputLocation,pageType):
		self.outputDir = outputLocation
		self.sep = os.sep
		self.font24 = Font(path='./fonts/tyepaloon.ttf',size=24)
		self.font60 = Font(path='./fonts/tyepaloon.ttf',size=60)
		#valid types "vert",'horiz','square'
		self.pageType = pageType
		self.typeSizing = ImageHandler.typeSize[pageType]

	def setImage(self,fileNameTuple):
		self.fileName = fileNameTuple[1]
		self.fileDirectory = fileNameTuple[0]
		self.currentImageFilePath = self.fileDirectory + self.sep + self.fileName

	def resizeAndOverlayBackground(self,backgroundFile):
		refSize = self.typeSizing
		with Image(filename=self.currentImageFilePath) as img:
			with Image(filename=backgroundFile) as bg_img:
				#inspect image for width and height
				if self.pageType == 'vert':
					img.resize(width=835,height=1115)
					if img.width > img.height:
						img.rotate(90)
					bg_img.composite(img,top=5,left=285)

				elif self.pageType == 'horiz':
					img.resize(width=1115,height=835)
					if img.width < img.height:
						img.rotate(90)
					bg_img.composite(img,top=5,left=5)

				elif self.pageType == 'square':
					img.resize(refSize[0],refSize[1])
					with Color('#00000080') as grey:
						with Drawing() as draw:
							draw.fill_color = grey
							draw.rectangle(left=23,top=857,right=258,bottom=1092)
							draw(img)
					bg_img.composite(img,top=5,left=5)
				else:
					return None
				bg_img.save(filename=self.outputDir+self.sep+'rsBG'+self.fileName)

	def addDateAndText(self,tweet,day,weekday,month):
		#MUST CALL setImage fist
		dayStr = '%02d' % (day)
		with Image(filename=self.currentImageFilePath) as img:
			#create day of week
			img.caption(weekday,left=90,top=65,width=108,height=56,font=self.font60,gravity='north_west')

			#create date of month
			img.caption(dayStr,left=116,top=116,width=72,height=56,font=self.font60,gravity='north_west')

			#create month 
			img.caption(month,left=90,top=172,width=108,height=56,font=self.font60,gravity='north_west')

			#create tweet 
			img.caption(tweet,left=23,top=475,width=232,height=500,font=self.font24,gravity='north_west')
		
			img.save(filename=self.outputDir + self.sep +  month + dayStr + weekday + "page.jpg")	
		return (self.outputDir, month + dayStr + weekday + "page.jpg")	
			
