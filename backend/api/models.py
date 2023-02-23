from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    age = models.IntegerField(null=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=32)


class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=300, null=True, blank=True)
    year = models.IntegerField(default=0)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='movies', null=True)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return self.title + '(' + str(self.year) + ')'


class Review(models.Model):
    rating = models.IntegerField(default=5)
    opinion = models.TextField(default='', max_length=1024)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')


class Actor(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    age = models.IntegerField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    movies = models.ManyToManyField(Movie)