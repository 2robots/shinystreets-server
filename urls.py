from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from shinystreetsapp import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^areas/$', views.AreaList.as_view()),
    url(r'^areas/(?P<pk>[0-9]+)/$', views.AreaDetail.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

    #admin interface
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns = format_suffix_patterns(urlpatterns)
