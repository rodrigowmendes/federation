from django.test import TestCase

from .models import Starship, Crewman, Species, Planet

# Create your tests here.
class StarshipModelTests(TestCase):

    def test_count_number_of_crew(self):
        # creating planets instances
        vulcan_planet = Planet.objects.create(planet_name='Vulcan')
        earth_planet = Planet.objects.create(planet_name='Earth')
        vulcan_planet.save()
        earth_planet.save()
        
        # creating species instances
        human = Species.objects.create(description='Human', planet_of_origin=earth_planet)
        vulcan = Species.objects.create(description='Vulcan', planet_of_origin=vulcan_planet)
        human.save()
        vulcan.save()
        
        # creating a startship instance
        starship = Starship.objects.create(name='USS Enterprise', record='NCC-1701')
        starship.save()

        # creating crewmen instances
        kirk = Crewman.objects.create(name='James Tiberius Kirk', species=human, starship=starship)
        spock = Crewman.objects.create(name='Spock', species=vulcan, starship=starship)
        scotty = Crewman.objects.create(name='Montgomery Scott', species=human, starship=starship)
        kirk.save()
        spock.save()
        scotty.save()

        self.assertIs(starship.count_number_of_crew(), 3)

