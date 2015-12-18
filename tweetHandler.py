import math
import random

class TweetHandler:
	def __init__(self, fileName, charsInLine, fontSize):
		self.fileName = fileName
		self.currIndex = 0
		self.charsInLine = charsInLine
		self.fontSize = fontSize
		self.dx = 0.597
		self.dy = 0.92

		self.tweets = []

		with open(fileName) as f:
			for line in f:
				line = line[:-1]
				self.tweets.append({'text': line, 'charLength': len(line), 'numLines': int(math.ceil(float(len(line)) / charsInLine))})

		self.randTweets = self.tweets
		random.shuffle(self.randTweets)

	def getTweet(self):
		for i in self.randTweets:
			yield i
	
	def getTweetText(self):
		for i in self.randTweets:
			yield i['text']

	def getWidth(self):
		return int(self.dx*self.fontSize*self.charsInLine) + 20

	def getHeight(self,numLines):
		return int(numLines*self.fontSize*self.dy) + 10


#tweets = TweetHandler('tweets.txt',23,60)

#print tweets.getHeight(3)
	

