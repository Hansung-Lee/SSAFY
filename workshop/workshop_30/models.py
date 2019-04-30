from django.db import models

# Create your models here.


class Hashtag(models.Model):
    content = models.CharField(max_length=50)
    
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    hashtag = models.ManyToManyField(Hashtag)
