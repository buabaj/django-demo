#inherit from django models and create model for car with name, color, type, description and price
from django.db import models

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
    