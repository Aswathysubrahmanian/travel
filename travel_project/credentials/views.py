from django.shortcuts import render

# Create your views here.
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                return redirect("reg")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"this email id already exist")
                return redirect("reg")
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                print("user created")

        else:
            messages.info(request,"password not matching")
            return redirect("reg")
        return redirect("login")
    return render(request,'register.html')


def login(request):
    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("home")
        else:
            messages.info(request,"invalid credentials")
            return redirect("login")
    return render(request,"login.html")

def logout(request):
    auth.logout(request,)
    return redirect("register")




#
#
# def operation(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#
#     return render(request,'operations.html',{'add':add,'sub':sub,'mul':mul,'div':div})