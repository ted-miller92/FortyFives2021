from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    eventTitle=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    date=models.DateField()
    time=models.TimeField()
    description=models.TextField()
    userId=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.eventTitle
    
    class Meta:
        db_table='event'
        verbose_name_plural='events'

class Venue(models.Model):
    venue=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    hours=models.CharField(max_length=255)

    def __str__(self):
        return self.venue

    class Meta:
        db_table='venue'
        verbose_name_plural='venues'