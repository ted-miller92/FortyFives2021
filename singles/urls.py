from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getevents/',views.getEvents, name='events'),
    path('getvenues/',views.getVenues, name='venues'),
    path('getfortyfives/',views.getFortyFives, name='fortyfives'),
    path('getrecordstores/',views.getRecordStores, name='recordstores'),
    path('fortyfivedetails/<int:id>', views.fortyFiveDetail, name='fortyfivedetails'),
    path('newEvent/', views.newEvent, name='newevent'),
    path('newFortyFive/', views.newFortyFive, name='newfortyfive'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]