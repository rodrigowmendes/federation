from django.contrib import admin

from .models import Planet, Species, Starship, Crewman


admin.site.register(Planet)
admin.site.register(Species)
admin.site.register(Starship)
admin.site.register(Crewman)
