from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FortyFive(models.Model):
    artistname=models.CharField(max_length=255)
    label=models.TextField(null=True, blank=True)
    year=models.TextField(null=True, blank=True)
    sideone=models.TextField(null=True, blank=True)
    sidetwo=models.TextField(null=True, blank=True)
    review=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.artistname
    
    class Meta:
        db_table='fortyfive'
        verbose_name_plural='fortyfives'

class RecordStore(models.Model):
    storename=models.CharField(max_length=255)
    storelocation=models.TextField(null=True, blank=True)
    businesshours=models.TextField(null=True, blank=True)
    website=models.URLField(null=True, blank=True)
    description=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.storename
    
    class Meta:
        db_table='recordstore'
        verbose_name_plural='recordstores'

class Venue(models.Model):
    venuename=models.CharField(max_length=255)
    venuelocation=models.TextField(null=True, blank=True)
    venueinfo=models.TextField(null=True, blank=True)
    website=models.URLField(null=True, blank=True)

    def __str__(self):
        return self.venuename
    
    class Meta:
        db_table='venue'
        verbose_name_plural='venues'

class Event(models.Model):
    eventname=models.CharField(max_length=255)
    venuelocation=models.ForeignKey(Venue, on_delete=models.DO_NOTHING)
    eventinfo=models.TextField(null=True, blank=True)
    eventdate=models.DateField()
    eventurl=models.URLField(null=True, blank=True)

    def __str__(self):
        return self.eventname
    
    class Meta:
        db_table='event'
        verbose_name_plural='events'