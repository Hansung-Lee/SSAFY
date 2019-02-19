from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    
class Choice(models.Model):
    content = models.CharField(max_length=100)
    votes = models.IntegerField()
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)