from django.db.models import Min
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DoorStatusSerializer, SensorDataSerializer
from django.apps import apps
from rest_framework import permissions
from .models import SensorData
from django.core import serializers


# Create your views here.

DoorStatus = apps.get_model('doorlog','DoorStatus')


class DoorStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = DoorStatus.objects.all().order_by('-date')
    serializer_class = DoorStatusSerializer


class SensorViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer


class SpaceAPI(viewsets.ViewSet):
    def list(self, request):
        sensorCats = {SensorData.TEMPERATURE, SensorData.HUMIDITY, SensorData.BAROMETER, SensorData.BETA_GAMMA, SensorData.MEMBER_COUNT, SensorData.CO2, SensorData.MAXPERSONS}

        doorStatus = DoorStatus.objects.latest('id')
        sensorsData = {}
        for sensorCat in sensorCats:
            sensors = SensorData.objects.filter(type=sensorCat)
            if len(sensors):
                sensorData = []
                for sensor in sensors:
                    sensorDict = {
                        "name": sensor.name,
                        "value": sensor.value,
                        "unit": sensor.unit,
                    }
                    if sensor.location is not None:
                        sensorDict.update({"location": sensor.location})
                    if sensor.description is not None:
                        sensorDict.update({"description": sensor.description})
                    sensorData.append(sensorDict)
                if (sensorCat == SensorData.BETA_GAMMA):
                    sensorsData.update({"radiation": {sensorCat: sensorData}})
                else:
                    sensorsData.update({sensorCat: sensorData})
        content = {
            "api": "0.13",
            "api_compatibility": ["14"],
            "space": "Nerdberg",
            "logo": "https://wiki.nerdberg.de/resources/assets/logo.png",
            "url": "https://www.nerdberg.de",
            "sensors": sensorsData,
            "location": {
                "address": "Jakobinenstraße 26, 90762 Fuerth, Germany",
                "lat": 49.47048,
                "lon": 11.0033
            },
            "contact": {
                "twitter": "@nerdbergev",
                "irc": "irc://irc.hackint.org/nerdberg",
                "ml": "freunde@lists.nerdberg.de",
                "email": "vorstand@lists.nerdberg.de",
                "phone": "+49 221 59619 6274"
            },
            "feeds": {
                "calendar": {
                    "type": "ical",
                    "url": "https://kalender.nerdberg.de/events.ics"
                }
            },
            "issue_report_channels": [
                "twitter"
            ],
            "ext_ccc": "chaostreff",
            "state": {
                "open": doorStatus.status=="open",
                "lastchange": int(doorStatus.date.timestamp()),
                "icon": {
                    "open": "https://wiki.nerdberg.de/images/f/f2/Nerdbergopen.png",
                    "closed": "https://wiki.nerdberg.de/images/a/a7/Nerdbergclose.png",
                }

            }
        }
        return Response(content)
