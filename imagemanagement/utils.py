
import requests
from PIL import Image
from StringIO import StringIO
import os
import sys
from .models import Photo




class imgProcesor(object):
	'''
	Class to process everything related to an image
	'''

	BASE_DIR = os.path.dirname(os.path.dirname(__file__))
	IMAGE_DIR = os.path.join("media","images")
	THUMB_DIR = os.path.join("media","thumbnails") 



	def __init__(self,url,title, desc):
		'''
		Specifies the attributes of the class (url, title, desc, request (for http requests), image)
		uses try except in case url parameter is invalid
		'''

		self.url = url
		self.title = title.lower()
		self.desc = desc
		try:
			self.request = requests.get(url)
			self.image = Image.open(StringIO(self.request.content))
		except:
			self.image = None
			self.request = None
			


	def downLoadImage(self):
		'''
		Checks if the url asigned to the imgProcesor is valid.
		Calls for storing an image in the media folder and and returns a result string
		'''

		if self.checkvalidurl():

			self.saveInServer()  
			self.saveInDB()

			return "The image "+self.title+\
			" was successfully rehosted"

		else:

			return "Image URL invalid please submit\
			 one that belongs to an image *"
		 	

	def saveInServer(self):
		'''
		Stores the image on the specified directory adding the title of the image as the name
		in the directory with its format extention and generates a thumbnail of the image
		'''

		self.image.save(self.IMAGE_DIR +'/'+self.changeSpc(self.title)+
			"."+self.image.format.lower(),self.image.format)

		#generate a thumbnail for the image
		self.makeThumb()



	def saveInDB(self):
		'''
		Creates an instances of Photo (representation of img in DB) and saves it into 
		the DB.
		'''

		p = Photo(url=self.url, title = self.title +"."+
		 self.image.format.lower(), desc= self.desc)

		p.save()




	def checkvalidurl(self):
		'''
		Checks if an url is valid and if it belongs to an image by using the http request header 
		Content-Type : image /
		'''

		if self.request == None :

			return False

		else:

			if self.request.status_code == requests.codes.ok and\
			 self.request.headers.get('Content-Type').split('/')[0] == 'image':

				return True

			else:

				return False

	

	def makeThumb(self):
		'''
		Creates thumbnail of an image making it square shape. If the image has same with an heigh it resizes it
		(it won't lose its aspect ratio) if not it crops it using cropit() to generate a nxn square thumb.
		'''

		thumb = self.image

		if self.image.size[0] != self.image.size[1]:

			thumb = self.cropIt()

	
		thumb.thumbnail((200,200),Image.ANTIALIAS)

		thumb.save(self.THUMB_DIR+'/thumb-'+self.changeSpc(self.title)+
			"."+self.image.format.lower(),self.image.format)




	def cropIt(self):
		'''
		Gets the nxn region to crop an image making it square to crop an image
		'''

	 	upper_x, upper_y, lower_x, lower_y = self.boxParamsCenter(self.image.size[0], self.image.size[1])

	 	box = (upper_x, upper_y,
	 	 lower_x, lower_y)

	 	region = self.image.crop(box)
	 	return region



	def boxParamsCenter(self,width,height):
		'''
		Returns an the value of the region limits for cropping depending if the image
		is on isLandsCape or not
		'''

		if self.islandscape(width, height):
			upper_x = int((width/2) - (height/2))
			upper_y = 0
			lower_x = int((width/2) + (height/2))
			lower_y = height
			return upper_x, upper_y, lower_x, lower_y

		else:
			upper_x = 0
			upper_y = int((height/2) - (width/2))
			lower_x = width
			lower_y = int((height/2) + (width/2))
			return upper_x, upper_y, lower_x, lower_y



	def islandscape(self,width,height):
		'''
		Returns if an image is lanscape
		'''

		if width >= height:

			return True

		else:

			return False



	def changeSpc(self,strg):
		'''Returns a string

		Replaces spaces by _ of a string
		'''

		li = []

		for char in strg:

			if char == " ":
				li.append('_')
			else:
				li.append(char)

		return "".join(strg)











