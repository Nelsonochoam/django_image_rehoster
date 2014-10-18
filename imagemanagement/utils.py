
import requests
from PIL import Image
from StringIO import StringIO
import os
import sys
from .models import Photo




class imgProcesor(object):
	#Image Procesing methods and Validations
	BASE_DIR = os.path.dirname(os.path.dirname(__file__))
	IMAGE_DIR = os.path.join("media","images")
	THUMB_DIR = os.path.join("media","thumbnails") 


	def __init__(self,url,title, desc):

		self.url = url
		self.title = title.lower()
		self.desc = desc
		self.request = requests.get(url)
		self.image = Image.open(StringIO(self.request.content))




	def downLoadImage(self):

		if self.checkValidUrl():

			self.saveInServer()  #validate if image saved in server then store in DB
			self.saveInDB()
		 	print >> sys.stderr, "Image confirmed"



	def saveInServer(self):

		finaltitle = []

		for char in self.title:

			if char == " ":
				finaltitle.append('_')
			else:
				finaltitle.append(char)

		finaltitle.append("."+self.image.format.lower())

		self.image.save(self.IMAGE_DIR +'/'+"".join(finaltitle),self.image.format)

		#generate a thumbnail for the image
		self.makeThumb()



	def saveInDB(self):

		p = Photo(url=self.url, title = self.title +"."+ self.image.format.lower(), desc= self.desc)
		p.save()




	def checkValidUrl(self):

		if self.request.status_code == requests.codes.ok:
		
			if self.request.headers.get('Content-Type').split('/')[0] == 'image':

				return True

		print >> sys.stderr, "Error confirming image"
		return False




	def makeThumb(self):

		thumb = self.image

		if self.image.size[0] != self.image.size[1]:

			thumb = self.cropIt()

	
		thumb.thumbnail((200,200),Image.ANTIALIAS)
		thumb.save(self.THUMB_DIR+'/thumb-'+self.title+"."+self.image.format.lower(),self.image.format)




	def cropIt(self):

	 	upper_x, upper_y, lower_x, lower_y = self.boxParamsCenter(self.image.size[0], self.image.size[1])
	 	box = (upper_x, upper_y, lower_x, lower_y)
	 	region = self.image.crop(box)
	 	return region



	def boxParamsCenter(self,width,height):

		if self.isLandsCape(width, height):
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



	def isLandsCape(self,width,height):

		if width >= height:

			return True

		else:

			return False









