from django.db import models

# Create your models here.


class Article(models.Model):
    content = models.CharField(max_length=254)


class Comments(models.Model):
    id_article = models.IntegerField(max_length=254),
    user = models.CharField(max_length=254),
    comment = models.TextField(),
    # foreign key a lo mejor?!
