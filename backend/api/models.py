from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=300)
    director = models.CharField(max_length=32)
    year = models.IntegerField(default=0)



