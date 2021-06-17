from django import forms
from .models import Event, Venue, FortyFive, RecordStore 

class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields='__all__'

class FortyFiveForm(forms.ModelForm):
    class Meta:
        model=FortyFive
        fields='__all__'