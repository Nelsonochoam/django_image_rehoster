from django.db import models

#Photo model
class Photo(models.Model):
	'''
	Photo model: represents an image in the DB
	attributes: title, description, url, timestamp
	'''

	title = models.CharField(
		max_length = 120, null = False, 
		blank = False)

	desc = models.CharField(
		max_length = 200, null = True, 
		blank = True)

	url = models.URLField(
		null=False, blank = False)

	timestamp = models.DateTimeField(
		auto_now_add=True, auto_now =False)


	def __unicode__(self):
		return self.title 