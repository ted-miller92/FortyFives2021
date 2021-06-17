from django.test import TestCase
from .models import Event, Venue, FortyFive, RecordStore
import datetime
from .forms import FortyFiveForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse

# Create your tests here.

class FortyFiveTest(TestCase):
    def setUp(self):
        self.artist=FortyFive(artistname='April Silva')
    
    def test_resourcestring(self):
        self.assertEqual(str(self.artist), 'April Silva')

    def test_table(self):
        self.assertEqual(str(FortyFive._meta.db_table), 'fortyfive')

class EventTest(TestCase):
    def setUp(self):
        self.event=Event(eventname='ECSC Weekender')
        self.event2=Event(eventname='ECSC', eventinfo='Party', eventdate=datetime.date(2021,6,16), eventurl='http://www.ecsc.com',)
    
    def test_eventstring(self):
        self.assertEqual(str(self.event), 'ECSC Weekender')

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event')        

class NewFortyFiveForm(TestCase):
    def test_fortyfiveform(self):
        data={
            'artistname':'April Silva', 
            'label':'Commonwealth', 
            'year':'1966',
            'sideone':'Under My Thumb',
            'sidetwo':'In Cold Blood',
            'review':'Stones cover'
        }
        form=FortyFiveForm (data)
        self.assertTrue(form.is_valid)         

class New_FortyFive_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='p@ssw0rd1')
        self.fortyfive=FortyFive(artistname='April Silva')
        self.newfortyfive=FortyFive(artistname='April Silva', label='Commonwealth', year='1966', sideone='Under My Thumb', sidetwo='In Cold Blood')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newfortyfive'))
        self.assertRedirects(response, '/accounts/login/?next=/singles/newFortyFive/')         