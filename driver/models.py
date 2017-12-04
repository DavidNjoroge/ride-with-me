from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django_google_maps import fields as map_fields


# Create your models here.
class Profile(models.Model):
    User=models.OneToOneField(User, on_delete=models.CASCADE)
    home=models.CharField(max_length=50)
    destination=models.CharField(max_length=50)
    number_plate=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    # pic
    capacity=models.IntegerField()

# @receiver(post_save,sender=User)
# def create_user_profile(instance):
#     if created:
    # Profile.objects.create(User=instance)

# @receiver(post_save,sender=User)
# def save_user_profile(sender,instance,**kwargs):
#     instance.profile.save()

# google map model<><><> i think<><><><>
class Home(models.Model):
    # address = map_fields.AddressField(max_length=30)
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
