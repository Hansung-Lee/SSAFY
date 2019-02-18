from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
    author = models.TextField()
    
    def __repr__(self):
        return f"<{self.title}>"
        
    def __str__(self):
        return f"<{self.title}>"