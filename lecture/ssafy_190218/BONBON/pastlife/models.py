from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.TextField()
    job = models.TextField()
    
    def __repr__(self):
        return f"<{self.name}: {self.job}>"
        
    def __str__(self):
        return f"<{self.name}: {self.job}>"