from rest_framework_mongoengine import serializers as mongoserializers

from .models import House

class HouseSerializer(mongoserializers.DocumentSerializer):

    class Meta:
        model = House
        fields = '__all__'

