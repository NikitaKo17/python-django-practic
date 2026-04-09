from django.db import models
from django.utils import timezone


class Animals(models.Model):
    name=models.CharField(max_length=255)
    species=models.CharField(max_length=255)
    age=models.IntegerField()
    health=models.CharField()
    def __str__(self):
        return self.name
    

class Enclosures(models.Model):
    description=models.CharField(max_length=255)
    size=models.IntegerField()
    def __str__(self):
        return self.description
    
# Create your models here.
