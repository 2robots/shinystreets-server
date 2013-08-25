# Create your views here.
from django.http import Http404, HttpResponse
from django.template import Context, loader

from shinystreetsapp.models import Area


def index(request):
    areas = Area.objects.all()
    t = loader.get_template('areas/index.html')
    c = Context({'object_list': areas})
    return HttpResponse(t.render(c))

def detail(request, slug):
	try:
		area = Area.objects.get(slug=slug)
	except Area.DoesNotExist:
		raise Http404
	t = loader.get_template('areas/detail.html')
	c = Context({'object': area})
	return HttpResponse(t.render(c))