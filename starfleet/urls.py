from django.conf.urls import url, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'starships', views.StarshipViewSet)
router.register(r'planets', views.PlanetViewSet)
router.register(r'species', views.SpeciesViewSet)
router.register(r'crewmen', views.CrewmanViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
