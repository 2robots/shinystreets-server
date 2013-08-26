from django.conf.urls import patterns, url

urlpatterns = patterns('shinystreetsapp.views',
    url(r'^areas/$', 'area_list'),
    url(r'^areas/(?P<pk>[0-9]+)/$', 'area_detail'),
)
