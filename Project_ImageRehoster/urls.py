from django.conf.urls import patterns, include, url
from django.contrib import admin
from imagemanagement import views


urlpatterns = patterns('',
    # Examples:
    # URL used for submiting images to the server
    url(r'^$', views.saveimage),
    # url used for displaying all the images or searching for a particular id
    url(r'^view/$', views.showImages),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
