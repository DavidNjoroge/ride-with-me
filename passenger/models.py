from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Passenger_Profile(models.Model):
    User=models.OneToOneField(User, on_delete=models.CASCADE)
    home=models.CharField(max_length=50)
    destination=models.CharField(max_length=50)
