from .models import Starship, Planet, Species, FleetMember
from rest_framework import viewsets
from . import serializers


class StarshipViewSet(viewsets.ModelViewSet):
    queryset = Starship.objects.all()
    serializer_class = serializers.StarshipSerializer


class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = serializers.PlanetSerializer


class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = serializers.SpeciesSerializer


class FleetMemberViewSet(viewsets.ModelViewSet):
    queryset = FleetMember.objects.all()
    serializer_class = serializers.FleetMemberSerializer
