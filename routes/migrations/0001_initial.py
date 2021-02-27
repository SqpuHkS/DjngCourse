# Generated by Django 3.1.6 on 2021-02-25 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities', '0001_initial'),
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Route name')),
                ('travel_times', models.PositiveSmallIntegerField(verbose_name='Travel times')),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_from_city_set', to='cities.city', verbose_name='From city')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_to_city_set', to='cities.city', verbose_name='To city')),
                ('trains', models.ManyToManyField(to='trains.Train', verbose_name='Trains list')),
            ],
            options={
                'verbose_name_plural': 'Routes',
                'ordering': ['travel_times'],
            },
        ),
    ]