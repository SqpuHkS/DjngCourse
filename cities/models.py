from django.db import models
from django.urls import reverse


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cities:detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Cities'
        ordering = ['name']