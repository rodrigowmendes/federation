from django.db import models


class Planet(models.Model):
    planet_name = models.TextField(max_length=50)

    def __str__(self):
        return self.planet_name


class Starship(models.Model):
    name = models.TextField(max_length=50)
    record = models.TextField(max_length=50)
    
    def count_number_of_crew(self):
        return Crewman.objects.filter(starship=self.id).count()

    def __str__(self):
        return '{0}, {1}'.format(
            self.name,
            self.record,
            self.number_of_crew
        )


class Species(models.Model):
    description = models.TextField(max_length=50)
    planet_of_origin = models.ForeignKey(Planet, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "species"

    def __str__(self):
        return '{0}, {1}'.format(
            self.description,
            self.planet_of_origin
        )


class Crewman(models.Model):
    name = models.TextField(max_length=50)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    starship = models.ForeignKey(Starship, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "crewmen"

    def __str__(self):
        return '{0}, {1}'.format(
            self.name,
            self.species,
            self.starship
        )
