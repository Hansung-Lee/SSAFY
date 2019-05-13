from django.db import models
from django.conf import settings


# Create your models here.
class Genre(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    movie_code = models.TextField()
    movie_name_ko = models.TextField()
    movie_name_en = models.TextField()
    showTm = models.TextField()
    openDt = models.TextField()
    watch_grade_nm = models.TextField()
    audience = models.IntegerField()
    actors = models.TextField()
    directors = models.TextField()
    description = models.TextField()
    poster_url = models.TextField()
    # genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    genre = models.TextField()
    def __str__(self):
        return self.movie_name_ko


class Score(models.Model):
    content = models.TextField()
    value = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
