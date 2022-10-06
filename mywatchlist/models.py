from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    have_watched = models.TextField() #booleanfield
    movie_title = models.TextField() #charfield
    movie_rating = models.IntegerField() #bisa di max ke 5
    movie_release = models.IntegerField() #datefield
    movie_review = models.TextField()
