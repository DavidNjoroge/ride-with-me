from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django_google_maps import fields as map_fields


# Create your models here.
class Profile(models.Model):
    User=models.OneToOneField(User, on_delete=models.CASCADE)
    # home=models.CharField(max_length=50)
    # destination=models.CharField(max_length=50)
    number_plate=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    profile_pic=models.ImageField(upload_to='profile/')
    capacity=models.IntegerField()

class LocationDriver(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    home_lat=models.FloatField()
    home_lng=models.FloatField()
    dest_lat=models.FloatField()
    dest_lng=models.FloatField()
    