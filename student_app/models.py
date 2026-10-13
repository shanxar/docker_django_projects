from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=10)
    age=models.PositiveIntegerField()

    def __str__(self):
        return self.name 
        
