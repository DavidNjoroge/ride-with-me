from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Passenger_Profile
# Create your views here.
@login_required(login_url='/accounts/login/')
def homeq(request):
    are=Passenger_Profile.objects.filter(User=request.user)
    # print(len(are))
    if len(are) !=1:
        return redirect('/passenger/setup/')
    return render(request,'homepass.html')

def setup(request):
    form=ProfileForm()
    if request.method=='POST':
        profile_form=ProfileForm(request.POST,files=request.FILES)
        if profile_form.is_valid:
            profile=profile_form.save(commit=False)
            profile.User=request.user
            profile.save()
            # print('<><><>half way<><>>')
    return render(request,'setup_profile_passenger.html',{'form':form})