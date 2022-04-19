from django.db import models


class Empleo(models.Model):
    foto = models.CharField(max_length=50, null = False, default = None)
    puesto = models.CharField(max_length=20, null = False, default = None)
    description = models.TextField(null = False, default = None)
    mail = models.EmailField(max_length=50, null = False, default = None)