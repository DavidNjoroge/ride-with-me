from django import forms
from django.contrib.auth.models import User
from .models import Passenger_Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Passenger_Profile
        fields=('home','destination')
    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)
        self.fields['home'].attrs={'id':'sddsfsdf'}