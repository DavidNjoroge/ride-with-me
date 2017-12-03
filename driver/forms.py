from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('home','destination','number_plate','color','capacity')
class ProfForm(forms.Form):
    home=forms.CharField(label='Home Area',max_length=30)
    destination=forms.CharField(label='Destination Area',max_length=30)
    plate=forms.CharField(label='Number plate',max_length=30)
    color=forms.CharField(label='Car color',max_length=30)
    capacity=forms.IntegerField(label='car capacity')
    