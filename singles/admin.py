from django.contrib import admin
from .models import Venue, Event, RecordStore, FortyFive

# Register your models here.
admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(RecordStore)
admin.site.register(FortyFive)

