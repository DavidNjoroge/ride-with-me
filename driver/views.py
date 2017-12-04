from django.shortcuts import render,redirect
from .forms import ProfileForm,ProfForm
from .models import Profile

# Create your views here.
def index(request):
    return render(request,'index.html')

# @login_required(login_url='')
def home(request):
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