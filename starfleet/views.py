from .models import StarshipClass, Starship, Planet, Idiom, Species, Crewman
from rest_framework import viewsets
from .serializers import StarshipClassSerializer, StarshipSerializer, PlanetSerializer, IdiomSerializer, \
    SpeciesSerializer, CrewmanSerializer


class StarshipClassViewSet(viewsets.ModelViewSet):
    queryset = StarshipClass.objects.all()
    serializer_class = StarshipClassSerializer


class StarshipViewSet(viewsets.ModelViewSet):
    queryset = Starship.objects.all()
    serializer_class = StarshipSerializer


class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer


class IdiomViewSet(viewsets.ModelViewSet):
    queryset = Idiom.objects.all()
    serializer_class = IdiomSerializer


class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer


class CrewmanViewSet(viewsets.ModelViewSet):
    queryset = Crewman.objects.all()
    serializer_class = CrewmanSerializer


