from django.shortcuts import render
#from rest_framework.viewsets import ModelViewSet
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet


from .models import House
from .serializers import HouseSerializer

# Create your views here.
class HouseViewSet(MongoModelViewSet):

    lookup_field = 'id'
    serializer_class = HouseSerializer
    queryset = House.objects.all()

    def get_queryset(self):
        return House.objects.all()
