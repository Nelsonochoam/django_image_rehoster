
from django import forms



class PhotoForm(forms.Form):
	'''
	Form for the image in the submit.html template
	'''

	title = forms.CharField(
		max_length=100, label = '',
		required=True, error_messages = {'required':'Please specify a title for your image *'},
		widget = forms.TextInput(attrs = {'class': 'search','placeholder':'Image title (Requiered)'}))
							

	url = forms.URLField(
		label='', max_length=200,
		required=True, error_messages = {'required':'Please specify the url of the image *'},
		widget = forms.TextInput(attrs = {'class': 'search','placeholder':'Image URL (Requiered)'}))



	desc = forms.CharField(
		label = '', max_length=100, 
		required=False, 
		widget = forms.TextInput(attrs = {'class': 'search','placeholder':'Image Description (Optional)'}))

	
		#pcfile = forms.FileFIeld(widget = forms.FIleInput())







		





