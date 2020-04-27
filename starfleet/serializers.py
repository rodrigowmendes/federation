from .models import Starship, Planet, Species, FleetMember
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


class FleetMemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FleetMember
        fields = (
            'name',
            'species',
            'starship'
        )
