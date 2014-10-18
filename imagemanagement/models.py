from django.db import models

# Create your models here.
class Photo(models.Model):
	#Title of the image
	title = models.CharField(max_length = 120, 
							 null = False, 
							 blank = False)
	#Desc of the image
	desc = models.CharField(max_length = 200, null = True, blank = True)
	#Url of the image / can't be null / required value 
	url = models.URLField(null=False, blank = False)
	#Time when the image was added/not when updated
	timestamp = models.DateTimeField(auto_now_add=True, auto_now =False)

	def __unicode__(self):
		return self.title 