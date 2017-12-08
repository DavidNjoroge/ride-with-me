from django import forms
from django.contrib.auth.models import User
from .models import Passenger_Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Passenger_Profile
        fields=('home','destination')