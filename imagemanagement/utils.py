
import requests
from PIL import Image
from StringIO import StringIO
import os
import sys
from .models import Photo



#Image Procesing methods and Validations
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
IMAGE_DIR = os.path.join("media","images")
THUMB_DIR = os.path.join("media","thumbnails") 




def checkValidUrl(url):
	r = requests.get(url)

	if r.status_code == requests.codes.ok:
		
		if r.headers.get('Content-Type').split('/')[0] == 'image':

			return True

	return False



def downLoadImage(url,title,desc):

	try:

		request = requests.get(url)

		if request.status_code == requests.codes.ok:

			im = Image.open(StringIO(request.content)) 
			
			return storeImage(im,title,desc,url)

		else:

			#print >> sys.stderr, "Error1"
			return "Error connectiong to client server please try again"

	except:

		return "Error connectiong to client server try again"

	



def storeImage(image,title,desc,url):

	try:

		finaltitle = []
		title = title.lower()

		for char in title:

			if char == " ":
				finaltitle.append('_')
			else:
				finaltitle.append(char)

		finaltitle.append("."+image.format.lower())

		title = "".join(finaltitle)

		#Store image information on DB
		imagemodel = Photo(title = title,desc = desc, url = url)
		imagemodel.save()

		#Store image on server / Generate a thumbnail
		image.save(IMAGE_DIR +'/'+title ,image.format)
		thumb = image
		thumb.thumbnail((200,200),Image.ANTIALIAS)
		thumb.save(THUMB_DIR+'/thumb-'+title,image.format)



		return "Your image was successfully Rehosted"

	except:

		return "Error Rehosting the image on the server please try again"















