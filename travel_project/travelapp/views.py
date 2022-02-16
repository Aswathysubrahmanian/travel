from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import place

# Create your views here.


def view(request):
    obj=place.objects.all()
    context={"result":obj}
    return render(request,"index.html",context)
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