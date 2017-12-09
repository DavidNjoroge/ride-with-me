from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Passenger_Profile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
    
    print(user_id)
    data = {'success': 'You have been successfully added to mailing list'}

    return JsonResponse(data)