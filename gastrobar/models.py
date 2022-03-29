from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Reservation(models.Model):
    name = models.CharField(max_length=20, null = False, default = None)
    mail = models.EmailField(max_length=50, null = False, default = None)
    phone = models.CharField(max_length=15, null = False, default = None)
    date = models.DateField(max_length=25, null = False, default = None)
    time = models.TimeField(max_length=5, null = False, default = None)
    count_p = models.IntegerField()


class Dish(models.Model):
    name = models.CharField(max_length=100, null = False, default = None)
    type = models.CharField(max_length=25, null = False, default = None)
    description = models.TextField(null = False, default = None)
    price = models.CharField(max_length=15, null = False, default = None)
    photo = models.CharField(max_length=12, null = False, default = None)
