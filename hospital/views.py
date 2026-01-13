from django.shortcuts import render,redirect
from hospital.models import User,Doctor,Apointment
from django.http import HttpResponse
from django.contrib.auth import authenticate

# Create your views here.

def index(request):
    user_visted = "Test User"
    context = {
        "user":user_visted
    }
    return HttpResponse(render(request,"index.html",context=context))

def home(request):
    print(request.user)
    return HttpResponse(render(request,"home.html",context={"user":request.user}))

def create_user(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        role = request.POST.get('role')
        email = request.POST.get('email')

        if(User.objects.filter(username=username).exists()):
            return HttpResponse({"detail":"Username already exist"})
        if(User.objects.filter(email = email).exists()):
            return HttpResponse({"detail":"Email Already exists"})
        
        user = User.objects.create(username=username,first_name=first_name,last_name=last_name,email=email,role=role)
        user.set_password(password)
        user.save()

        return redirect(to="login")#login page
    
    return HttpResponse(render(request,"register.html"))


def login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(username = username,password = password)
            if user is not None:
                print("Logged succesfully")
                return redirect(to="home")
            return redirect(to="login")
        except:
            return redirect("login"),{"message":"Invalid credentials"}


    return HttpResponse(render(request,"login.html"))
