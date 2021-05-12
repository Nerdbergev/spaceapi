from rest_framework import serializers
from django.apps import apps
from .models import SensorData

DoorStatus = apps.get_model('doorlog', 'DoorStatus')

class DoorStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DoorStatus
        fields = ['date', 'status']


class SensorDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'
