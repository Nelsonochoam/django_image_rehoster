
from django import forms
from .models import Photo


class PhotoForm(forms.Form):

	title = forms.CharField(max_length=100,
							label = '',
							required=True,
							error_messages = {'required':'Please specify a Title for your image'},
							widget = forms.TextInput(attrs = {'class': 'search',
															  'placeholder':'Image Title'}))
							

	url = forms.URLField(label='',
						  max_length=200,
						  required=True,
						  widget = forms.TextInput(attrs = {'class': 'search',
															  'placeholder':'Image URL'}))



	desc = forms.CharField(label = '',
						    max_length=100, 
						    required=False,
						    widget = forms.TextInput(attrs = {'class': 'search',
															  'placeholder':'Image Description'}))


	'''def clean_url(self):

		cd = self.cleaned_data
		url = cd.get('url')

		#if not a valid url
		if not checkValidUrl(url):

			raise forms.ValidationError('The Url provided must be from an Image ')
		
		return url'''

		





