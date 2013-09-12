from shinystreetsapp.models import Area
from shinystreetsapp.serializers import AreaSerializer
from rest_framework import generics


class AreaList(generics.ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class AreaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer