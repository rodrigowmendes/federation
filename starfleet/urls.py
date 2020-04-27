from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'starships', views.StarshipViewSet)
router.register(r'planets', views.PlanetViewSet)
router.register(r'species', views.SpeciesViewSet)
router.register(r'fleetmember', views.FleetMemberViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
