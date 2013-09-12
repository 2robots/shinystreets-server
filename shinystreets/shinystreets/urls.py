from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
admin.autodiscover()

urlpatterns = patterns('shinystreetsapp.views',
    url(r'^areas/$', 'area_list'),
    url(r'^areas/(?P<pk>[0-9]+)/$', 'area_detail'),

    #admin interface
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns = format_suffix_patterns(urlpatterns)
