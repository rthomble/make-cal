import random
import os


class FileNameHandler():
	def __init__(self,pathToDirectory):
		self.fileSep = os.path.sep
		self.directoryPath = pathToDirectory
		self.filePool = [i for i in os.listdir(pathToDirectory) if i[0] != '.']
		self.filePoolRandom = self.filePool
		random.shuffle(self.filePoolRandom)		

	def returnRandomFile(self):
		for i in self.filePoolRandom:
			yield (self.directoryPath, i)
	def returnFile(self):
		for i in self.filePool:
			yield (self.directoryPath, i)
	

#f = FileNameHandler("/Users/rthomble/Documents/Programming/cal/dPhoto/square")

#z = f.returnRandomFile()
#print next(z)
#print next(z)
#print next(z)
#print next(z)
