from secrets import choice
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from tinymce.models import HTMLField

from .pokemon_names import pokemon_choices
from .pokemon_natures import nature_choices
from .system_choices import system_choices

# Create your models here.


class Offer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pokemon_name = models.CharField(max_length=4, choices=pokemon_choices, default=1)
    pokemon_level = models.IntegerField(
        default=1, validators=[MaxValueValidator(100), MinValueValidator(1)]
    )
    pokemon_shiny = models.BooleanField(default=False)
    pokemon_ability = models.CharField(blank=True, max_length=200)
    pokemon_nature = models.CharField(max_length=2, choices=nature_choices, blank=True)
    system = models.CharField(max_length=1, choices=system_choices, default=5)
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lon = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    html = HTMLField()

    def __str__(self):
        return f"{self.pokemon_name} de niveau {self.pokemon_level} proposé par {self.user}."


class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pokemon_name = models.CharField(max_length=4, choices=pokemon_choices, default=1)
    pokemon_shiny = models.BooleanField(default=False)
    pokemon_ability = models.CharField(blank=True, max_length=200)
    pokemon_nature = models.CharField(max_length=2, choices=nature_choices, blank=True)
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lon = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    html = HTMLField()

    def __str__(self):
        return f"{self.pokemon_name} cherché par {self.user}."
