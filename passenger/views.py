from django.shortcuts import render

# Create your views here.
def homeq(request):
    return render(request,'homepass.html')