from django.db import models

# Create your models here.

class BookModel(models.Model):
    title = models.CharField(max_length=50)
    Author = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    cover_img = models.ImageField()
    rating = models.FloatField()