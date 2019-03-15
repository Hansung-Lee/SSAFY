from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"


class Movie(models.Model):
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=140)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class Score(models.Model):
    content = models.CharField(max_length=140)
    score = models.IntegerField()
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content}"
