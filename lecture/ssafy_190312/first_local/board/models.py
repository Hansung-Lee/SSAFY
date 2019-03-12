from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.TextField(default='')
    content = models.TextField(default='')
    like = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id}: {self.title[:20]}'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.article.title}: {self.content}'
