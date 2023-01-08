from django.db import models
from datetime import datetime

class Pilot(models.Model):
    pilotId = models.CharField(max_length=100)
    firstName = models.TextField(blank=False)
    lastName = models.TextField(blank=False)
    phoneNumber = models.CharField(max_length=100)
    createdDt = models.DateTimeField(default=datetime.now)
    email = models.CharField(max_length=100)
    closest_distance = models.FloatField(default=100000)
    last_seen = models.DateTimeField(default=datetime.now)
    drone_serial_number = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'pilots'
        ordering = ['last_seen']
