from django.db import models

# Create your models here.


class Article(models.Model):
    content = models.TextField()


class Comments(models.Model):
    id_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.CharField(max_length = 20),
    comment = models.TextField()