from django.conf.urls import patterns, include, url
from django.contrib import admin
from imagemanagement import views


urlpatterns = patterns('',
    # Examples:
    # URL used for submiting images to the server
    (r'^', include('imagemanagement.urls')),


    url(r'^admin/', include(admin.site.urls)),
)


