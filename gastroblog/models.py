from django.db import models

# Create your models here.


class Article(models.Model):
    content = models.TextField(null = False, default = None)


class Comments(models.Model):
    id_article = models.ForeignKey(Article, on_delete=models.CASCADE, null = False, default = None)
    user = models.CharField(max_length = 20, null = False, default = None)
    comment = models.TextField(null = False, default = None)