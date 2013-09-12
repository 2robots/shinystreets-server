# Create your views here.
from django.http import Http404, HttpResponse
from django.template import Context, loader
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shinystreetsapp.models import Area
from shinystreetsapp.serializers import AreaSerializer


@api_view(['GET', 'POST'])
def area_list(request):
    """
    List all areas, or create a new snippet.
    """
    if request.method == 'GET':
        areas = Area.objects.all()
        serializer = AreaSerializer(areas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AreaSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def area_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """              
    try:
        area = Area.objects.get(pk=pk)
    except Area.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AreaSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AreaSerializer(snippet, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        area.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)