from django.conf.urls import patterns, include, url


urlpatterns = patterns('imagemanagement.views',

    url(r'^$', 'saveimage'),
    url(r'^view/$', 'showimages'),
)
