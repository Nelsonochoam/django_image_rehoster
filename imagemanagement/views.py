from django.shortcuts import render
from .forms import PhotoForm
from PIL import Image
from .models import Photo
from .utils import *


# missing to validate that the same image doesnt exist2 nor in the folder or server


# Create your views here.
#Considering the main page is submit  SOME VALIDATION ERRORS
def saveimage(request):
	#If a post was submited from the submit.html
	#Photo.objects.all().delete()
	if request.method == "POST":

		form = PhotoForm(request.POST)
		
		if form.is_valid():
			
			cd = form.cleaned_data


			#statusmsg =  downLoadImage(cd['url'],cd['title'],cd['desc'])
			process = imgProcesor(cd['url'],cd['title'],cd['desc'])
			process.downLoadImage()



			form = PhotoForm()
			return render(request,"submit.html",{'form':form})# Hide the text after it shows

		else: # Form has errors
			return render(request,"submit.html",{'form':form})

	form = PhotoForm()

	return render(request,"submit.html",{'form':form})
	



def showImages(request):

	if 'im_id' in request.POST:

		image_id = request.POST['im_id']

		title = image_id.replace(" ","_")

		image_list = Photo.objects.filter(title__contains = title)


	else:


		image_list = Photo.objects.all()

	
	return render(request, "view.html",{"ImgList":image_list})















