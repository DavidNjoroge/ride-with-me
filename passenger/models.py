from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Passenger_Profile(models.Model):
    User=models.OneToOneField(User, on_delete=models.CASCADE)
    home=models.CharField(max_length=50)
    destination=models.CharField(max_length=50)
    home_lat=models.FloatField()

class Location(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    home_lat=models.FloatField()
    home_lng=models.FloatField()
    dest_lat=models.FloatField()
    dest_lng=models.FloatField()
    
