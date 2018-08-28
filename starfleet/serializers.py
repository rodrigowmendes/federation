from .models import StarshipClass, Starship, Planet, Idiom, Species, Crewman
from rest_framework import serializers


class StarshipClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StarshipClass
        fields = ('description',)


class StarshipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Starship
        fields = ('name', 'record', 'starship_class')


class PlanetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Planet
        fields = ('planet_name',)


class IdiomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Idiom
        fields = ('description',)


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
            'idiom',
            'starship'
        )









