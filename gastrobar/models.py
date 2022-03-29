from django.db import models

# Create your models here.


class Reservation(models.Model):
    name = models.CharField(max_length=20),
    mail = models.EmailField(max_length=50),
    phone = models.CharField(max_length=15),
    date = models.DateField(max_length=25),
    time = models.TimeField(max_length=5),
    count_p = models.IntegerField()


class Dish(models.Model):
    name = models.CharField(max_length=100),
    type = models.CharField(max_length=25)
    description = models.TextField(),
    price = models.CharField(max_length=15),
    photo = models.IntegerField(max_length=12)
