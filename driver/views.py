from django.shortcuts import render,redirect
from .forms import ProfileForm
from .models import Profile,LocationDriver
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):

    return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def home(request):
    are=Profile.objects.filter(User=request.user)
    print(len(are))
    if len(are) !=1:
        return redirect('/driver/setup/')

    
    return render(request,'home.html')

def setup(request):
    form=ProfileForm()
    if request.method=='POST':
        profile_form=ProfileForm(request.POST,files=request.FILES)
        print('<><><>half way<><>>')
    return render(request,'setup_profile.html',{'form':form})

def create_profile(request):
    print ('<><><><><almost there<><><><><')
    form=ProfileForm()
    if request.method=='POST':
        profile_form=ProfileForm(request.POST)
        # profile_form.User=request.user
        # profile_form.Profile.Create()
        Profile.objects.create(User=request.user,home=profile_form.data['home'],number_plate=profile_form.data['number_plate'],destination=profile_form.data['destination'],color=profile_form.data['color'],capacity=profile_form.data['capacity'])

        home=profile_form.data['capacity']
        print(profile_form.data['number_plate'])
    return redirect('homedr')
def edit_profile(request):
    form=ProfileForm()
    if request.method=='POST':
        profile_form=ProfileForm(request.POST,instance=request.user.profile,files=request.FILES)
        
        print('<><><>almost<><><><>')
        if profile_form.is_valid():
            prof=profile_form.save(commit=False)
            prof.User=request.user
            prof.save()
            print('<><><>almost almost <><><><>')
            
            
    return render(request,'edit_profile.html',{'form':form})

def edit_location(request):
    return render(request,'edit_location.html')


@csrf_exempt
def ajax_locale(request):
    home_lat=request.POST.get('home_lat')
    home_lng=request.POST.get('home_lng')
    dest_lat=request.POST.get('dest_lat')
    dest_lng=request.POST.get('dest_lng')
    user_id=request.POST.get('user_id')
    print(user_id)
    # profile_up=Passenger_Profile()
    new_location=LocationDriver(home_lat=home_lat,home_lng=home_lng,dest_lat=dest_lat,dest_lng=dest_lng,user=request.user)
    # new_location.save()
    current_user=User.objects.get(pk=user_id) 
    current_user.locationdriver.home_lat=home_lat
    current_user.locationdriver.home_lng=home_lng
    current_user.locationdriver.dest_lat=dest_lat
    current_user.locationdriver.dest_lng=dest_lng
    
    current_user.locationdriver.save()
    data = {'success': 'your location has been succesfully saved'}

    return JsonResponse(data)