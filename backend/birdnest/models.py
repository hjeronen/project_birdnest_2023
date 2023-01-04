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

    class Meta:
        db_table = 'pilots'

class Drone(models.Model):
    serialNumber = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    mac = models.CharField(max_length=100)
    ipv4 = models.CharField(max_length=100)
    ipv6 = models.CharField(max_length=100)
    firmware = models.CharField(max_length=100)
    positionY = models.FloatField()
    positionX = models.FloatField()
    altitude = models.FloatField()
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)

    class Meta:
        db_table = 'drones'