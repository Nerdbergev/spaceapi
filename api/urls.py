from django.urls import include, path
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'doorstatus', views.DoorStatusViewSet)
router.register(r'sensors', views.SensorViewSet)
router.register(r'space', views.SpaceAPI, 'Spaceapi')



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
