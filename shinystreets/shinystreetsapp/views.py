from shinystreetsapp.models import Area
from shinystreetsapp.serializers import AreaSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AreaList(APIView):
    """
    List all areas, or create a new area.
    """
    def get(self, request, format=None):
        areas = Area.objects.all()
        serializer = AreaSerializer(areas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AreaSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AreaDetail(APIView):
    """
    Retrieve, update or delete an area instance.
    """
    def get_object(self, pk):
        try:
            return Area.objects.get(pk=pk)
        except Area.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        area = self.get_object(pk)
        serializer = AreaSerializer(area)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        area = self.get_object(pk)
        serializer = AreaSerializer(area, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Area(serializer.data)
        return Area(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        area = self.get_object(pk)
        area.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)