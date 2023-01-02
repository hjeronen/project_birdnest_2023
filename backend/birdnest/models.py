from django.db import models
from django.utils import timezone

class Pilot(models.Model):
    pilotId = models.CharField(max_length=100)
    firstName = models.TextField(blank=False)
    lastName = models.TextField(blank=False)
    phoneNumber = models.CharField(max_length=100)
    createdDt = models.DateTimeField(default=timezone.now)
    email = models.CharField(max_length=100)

    class Meta:
        db_table = 'pilots'
