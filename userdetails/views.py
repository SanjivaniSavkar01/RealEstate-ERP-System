from django.shortcuts import render
from django.http import HttpResponse
from .models import REUser

# Create your views here.
def home(request):
    return render(request ,"userdetails/home.html" )

def login(request):
    if request.method=="POST":
            username=request.POST.get("username")
            password=request.POST.get("password")
    
            user=REUser.objects.filter(
                username=username,
                password=password
            ).first()

            if user:
             return render(request, "userdetails/home.html", {
                 "smsg":f"login success for user:{username}"
             })
            else:
             return render(request, "userdetails/login.html", {
                "emsg":"invalid user login failed for user"
            })
    return render(request, "userdetails/login.html" )

def registration(request):
    if request.method=="POST":
        fullname=request.POST.get("fullname")
        mobileno=request.POST.get("mobileno")
        username=request.POST.get("username")
        password=request.POST.get("password")

        REUser.objects.create(
            fullname=fullname,
            mobileno=mobileno,
            username=username,
            password=password
        )
        return render(request, "userdetails/login.html")
    return render(request , "userdetails/registration.html" )
 