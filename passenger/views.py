from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Passenger_Profile,Location
from driver.models import LocationDriver
from django.http import JsonResponse
from django.contrib.auth.models import User
from driver.models import Profile
from django.views.decorators.csrf import csrf_exempt
from .serializer import DriverSerializer
# Create your views here.
@login_required(login_url='/accounts/login/')
def homeq(request):
    are=Passenger_Profile.objects.filter(User=request.user)
    # print(len(are))
    if len(are) !=1:
        return redirect('/passenger/setup/')
    drivers=Profile.objects.all()
    print(len(drivers))
    return render(request,'homepass.html',{'drivers':drivers})

def setup(request):
    form=ProfileForm()
    if request.method=='POST':
        profile_form=ProfileForm(request.POST,files=request.FILES)
        if profile_form.is_valid:
            profile=profile_form.save(commit=False)
            profile.User=request.user
            profile.save()
    return render(request,'setup_profile_passenger.html',{'form':form})
def edit_profile(request):
    form=ProfileForm()
    if request.method=='POST':
        profile_form=ProfileForm(request.POST,instance=request.user.passenger_profile)

        print('<><><>almost<><><><>')
        if profile_form.is_valid():
            prof=profile_form.save(commit=False)
            prof.User=request.user
            # prof.save()
            print('<><><>almost almost <><><><>')
    
    return render(request,'edit_profile_passenger.html',{'form':form})
@csrf_exempt
def ajax_locale(request):
    home_lat=request.POST.get('home_lat')
    home_lng=request.POST.get('home_lng')
    dest_lat=request.POST.get('dest_lat')
    dest_lng=request.POST.get('dest_lng')
    user_id=request.POST.get('user_id')

    profile_up=Passenger_Profile()
    new_location=Location(home_lat=home_lat,home_lng=home_lng,dest_lat=dest_lat,dest_lng=dest_lng)
    current_user=User.objects.get(pk=user_id) 
    current_user.location.home_lat=home_lat
    current_user.location.home_lng=home_lng
    current_user.location.dest_lat=dest_lat
    current_user.location.dest_lng=dest_lng
    
    current_user.location.save()
    data = {'success': 'your location has been succesfully saved'}

    return JsonResponse(data)

def ajax_driver(request):
    all_drivers=LocationDriver.objects.all()
    serializers= DriverSerializer(all_drivers,many=True)
    return JsonResponse(serializers.data)