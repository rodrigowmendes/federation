from .models import Starship, Planet, Species, Crewman
from rest_framework import serializers


class StarshipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Starship
        fields = ('name', 'record')


class PlanetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Planet
        fields = ('planet_name',)


class SpeciesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Species
        fields = ('description', 'planet_of_origin')


class CrewmanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Crewman
        fields = (
            'name',
            'species',
            'starship'
        )
