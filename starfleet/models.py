from django.db import models


class StarshipClass(models.Model):
    description = models.TextField(max_length=50)

    def __str__(self):
        return self.description


class Planet(models.Model):
    planet_name = models.TextField(max_length=50)

    def __str__(self):
        return self.planet_name


class Idiom(models.Model):
    description = models.TextField(max_length=50)

    def __str__(self):
        return self.description


class Starship(models.Model):
    name = models.TextField(max_length=50)
    record = models.TextField(max_length=50)
    starship_class = models.ForeignKey(StarshipClass, on_delete=models.CASCADE)

    def __str__(self):
        return '{0}, {1}'.format(
            self.name,
            self.record,
            self.starship_class
        )


class Species(models.Model):
    description = models.TextField(max_length=50)
    planet_of_origin = models.ForeignKey(Planet, on_delete=models.CASCADE)

    def __str__(self):
        return '{0}, {1}'.format(
            self.description,
            self.planet_of_origin
        )


class Crewman(models.Model):
    name = models.TextField(max_length=50)
    species = models.ManyToManyField(Species)
    idiom = models.ManyToManyField(Idiom)
    starship = models.ForeignKey(Starship, on_delete=models.CASCADE)

    def __str__(self):
        return '{0}, {1}'.format(
            self.name,
            self.species,
            self.idiom,
            self.starship
        )


