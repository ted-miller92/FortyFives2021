from django import forms
from .models import Event, Venue

class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields='__all__'