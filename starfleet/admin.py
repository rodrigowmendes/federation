from django.contrib import admin

from .models import StarshipClass, Planet, Idiom, Species, Starship, Crewman


admin.site.register(StarshipClass)
admin.site.register(Planet)
admin.site.register(Idiom)
admin.site.register(Species)
admin.site.register(Starship)
admin.site.register(Crewman)

