from django.shortcuts import render
from .forms import ProfileForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def setup(request):
    form=ProfileForm()
    return render(request,'setup_profile.html',{'form':form})