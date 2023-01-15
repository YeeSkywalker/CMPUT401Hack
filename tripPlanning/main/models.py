from datetime import datetime
from django.db import models

# Create your models here.
class Trip(models.Model):
    addedTime = models.DateTimeField(default=datetime.now())
    origin = models.CharField(max_length=100,default='null')
    destination = models.CharField(max_length=100)
    departureDate = models.DateTimeField(default='')

    def __str__(self):
        return self.destination
