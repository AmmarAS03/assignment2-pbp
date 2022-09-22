from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    have_watched = models.TextField()
    movie_title = models.TextField()
    movie_rating = models.IntegerField()
    movie_release = models.IntegerField()
    movie_review = models.TextField()
