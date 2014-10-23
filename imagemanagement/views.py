from django.shortcuts import render
from .forms import PhotoForm
from PIL import Image
from .models import Photo
from .utils import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def saveimage(request):
	'''
	Method called when the submit view is loaded  takes the data from the photo form and
	downloads and saves the image into the server
	'''
	Photo.objects.all().delete()
	if request.method == "POST":

		form = PhotoForm(request.POST)
		
		if form.is_valid():
			
			cd = form.cleaned_data


			
			process = imgProcesor(cd['url'],cd['title'],
								  cd['desc'])

			msg = process.downLoadImage()



			form = PhotoForm()
			return render(request,"submit.html",{'form':form,'Msg':msg})# Hide the text after it shows

		else: 

			return render(request,"submit.html",{'form':form})

	form = PhotoForm()

	return render(request,"submit.html",{'form':form})
	



def showimages(request):
	'''
	Method for displaying and searching the images stored on server
	includes pagination
	'''

	message = None;

	if 'im_id' in request.POST:

		image_id = request.POST['im_id']

		title = image_id.replace(" ","_")

		image_list = Photo.objects.filter(title__contains = title)

		if not image_list:

			message = "Your search returned no results"

	else:

		image_list = Photo.objects.all()

	#Pagination Feature
	paginator = Paginator(image_list,4)  #Number of items per page
	page_num = request.GET.get("page",1)

	try:
		page = paginator.page(page_num)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	except PageNotAnInteger:
		page = paginator.page(1)



	
	return render(request, "view.html",{"ImgList":image_list,
				 "Msg":message, "page":page})















