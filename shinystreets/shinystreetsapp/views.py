# Create your views here.
from django.http import Http404, HttpResponse
from django.template import Context, loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from shinystreetsapp.models import Area
from shinystreetsapp.serializers import AreaSerializer

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

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def area_list(request):
    """
    List all areas, or create a new area.
    """
    if request.method == 'GET':
        areas = Area.objects.all()
        serializer = AreaSerializer(areas, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AreaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def area_detail(request, pk):
    """
    Retrieve, update or delete an area.
    """
    try:
        areas = Area.objects.get(pk=pk)
    except Area.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AreaSerializer(areas)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AreaSerializer(areas, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        else:
            return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        areas.delete()
        return HttpResponse(status=204)