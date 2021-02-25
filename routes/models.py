from django.db import models

from cities.models import City
from trains.models import Train


class Route(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Route name')
    travel_times = models.PositiveSmallIntegerField(verbose_name='Travel times')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='route_from_city_set', verbose_name='From city')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='route_to_city_set', verbose_name='To city')
    trains = models.ManyToManyField(Train, verbose_name='Trains list')



    def __str__(self):
        return f'Route {self.name} from city {self.from_city}'


    class Meta:
        verbose_name_plural = 'Routes'
        ordering = ['travel_times']
