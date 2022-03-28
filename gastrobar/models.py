from django.db import models

# Create your models here.


class Reservation(models.Model):
    name = models.CharField(max_length=254),
    mail = models.EmailField(max_length=254),
    phone = models.CharField(max_length=15),
    date = models.DateField(max_length=20),  # auto_now_add = True, blank=True,
    time = models.TimeField(max_length=20),  # auto_now_add = True, blank=True,
    count_p = models.IntegerField(max_length=12)


class Dish(models.Model):
    name = models.CharField(max_length=254),
    description = models.TextField(),
    price = models.CharField(max_length=15),
    photo = models.IntegerField(max_length=12)
