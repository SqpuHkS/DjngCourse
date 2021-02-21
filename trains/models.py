from django.db import models

from cities.models import City


class Train(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Train name')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Travel time')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='from_city_set', verbose_name='From which city')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='to_city_set', verbose_name='To which city')

    def __str__(self):
        return f'Train №{self.name} from city {self.from_city}'

    class Meta:
        verbose_name_plural = 'Trains'
        ordering = ['travel_time']