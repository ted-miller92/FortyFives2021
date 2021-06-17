from django.shortcuts import get_object_or_404, render
from .models import Event, Venue, FortyFive, RecordStore 
from .forms import EventForm, FortyFiveForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index (request):
    return render(request, 'singles/index.html')

def getEvents(request):
    event_list=Event.objects.all()
    return render(request, 'singles/events.html', {'event_list': event_list})

def getVenues(request):
    venue_list=Venue.objects.all()
    return render(request, 'singles/venues.html', {'venue_list': venue_list})

def getFortyFives(request):
    fortyfive_list=FortyFive.objects.all()
    return render(request, 'singles/fortyfives.html', {'fortyfive_list': fortyfive_list})

def fortyFiveDetail(request, id):
    fortyfive=get_object_or_404(FortyFive, pk=id)
    return render(request, 'singles/fortyfivedetail.html', {'fortyfive': fortyfive})    

def getRecordStores(request):
    recordstore_list=RecordStore.objects.all()
    return render(request, 'singles/recordstores.html', {'recordstore_list': recordstore_list})

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

@login_required
def newFortyFive(request):
     form=FortyFiveForm
     if request.method=='POST':
          form=FortyFiveForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=FortyFiveForm()
     else:
          form=FortyFiveForm()
     return render(request, 'singles/newfortyfive.html', {'form': form})

def loginmessage(request):
    return render(request, 'singles/loginmessage.html')

def logoutmessage(request):
    return render(request, 'singles/logoutmessage.html')     
