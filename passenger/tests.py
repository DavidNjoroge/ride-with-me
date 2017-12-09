from django.test import TestCase
from .models import Location
from django.contrib.auth.models import User
# Create your tests here.

class LocationTestClass(TestCase):
    def setUp(self):
        self.david=User(username='davy', password='sdfsdfds')
        self.david.save()
        self.new_location=Location(user=self.david,home_lat=12.5,home_lng=12.5,dest_lat=12.5,dest_lng=12.5)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))

    def test_get_all_locations(self):
        self.assertTrue(len(locations)>0)