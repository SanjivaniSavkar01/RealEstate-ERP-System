from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("welcome to real estate home !")

def registration(request):
    return render(request , "sitedetails/registration.html")
 