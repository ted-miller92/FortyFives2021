from django.shortcuts import render
from .models import Event, Venue
from .forms import EventForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index (request):
    return render(request, 'singles/index.html')

def getevents(request):
    event_list=Event.objects.all()
    return render(request, 'singles/events.html', {'event_list' : event_list})

@login_required
def newEvent(request):
     form=EventForm
     if request.method=='POST':
          form=EventForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=EventForm()
     else:
          form=EventForm()
     return render(request, 'singles/newevent.html', {'form': form})

def loginmessage(request):
    return render(request, 'singles/loginmessage.html')

def logoutmessage(request):
    return render(request, 'singles/logoutmessage.html')