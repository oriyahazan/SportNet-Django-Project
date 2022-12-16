from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, User, Mission, Event
from .forms import RegisterForm
from datetime import datetime
from django.db.models import Q
from . import forms #

def home(request):
    context= {
        'posts' : Post.objects.all()
    }
    return render(request , 'blog/HomePage.html' , context)

def community(request):
    return render(request , 'blog/HomePageCommunity.html')

def organization(request):
    return render(request , 'blog/HomePageOrganization.html')

def AllDocOrg(request):
    return render(request , 'blog/AllDocOrg.html')    

def missions(request):
    missions =  Mission.objects.all().order_by('title')
    return render(request , 'blog/MissionPage.html' ,{'missions': missions})   


def AllDocAdm(request):
    return render(request , 'blog/AllDocAdm.html')    

def ComUserPage(request):
    comuser = User.objects.filter(role = 'community').order_by('full_name')
    return render(request , 'blog/ComUserPage.html' ,{'comuser': comuser})

def admin(request):
    return render(request , 'blog/HomePageAdmin.html')

def posts(request):
    posts =  Post.objects.all().order_by('title')
    return render(request , 'blog/posts_page.html' ,{'posts': posts})

def about(request):
    return HttpResponse('<h1>Blog About</h1>')

def CreatEvent(request):
    formE = forms.EventForm(request.POST)
    if request.method == 'POST':
            formE.save()
            return render(request,'blog/HomePageOrganization.html')
    else:
        print('invalid')
    return render(request , 'blog/CreatEvent.html',{'formE':formE})

def CreatMission(request):
    formM = forms.MissionForm(request.POST)
    if request.method == 'POST':
            formM.save()
            return render(request,'blog/HomePageAdmin.html')
    else:
        print('invalid')
    return render(request , 'blog/CreatMission.html',{'formM':formM})        


def register(request):
    form = forms.RegisterForm(request.POST)
    if request.method == 'POST':
            form.save()
            return render(request,'blog/HomePage.html')
    else:
        print('invalid')

    return render(request , 'blog/register.html' , {'form':form})


def login(request):
        if request.method == 'POST':
            #email = request.POST.get('Email')
            full_name = request.POST.get('full_name')
            password = request.POST.get('Password')
            mydata = User.objects.filter(Q(full_name=full_name) & Q(password=password)).values()
            print(full_name)
            print(password)
            if mydata.filter(role='community'):
                return render(request, 'blog/HomePageCommunity.html')
            if mydata.filter(role='organization'):
                return render(request, 'blog/HomePageOrganization.html')
            if mydata.filter(role='admin'):
                return render(request, 'blog/HomePageAdmin.html')
            else:
                print("someone tried to login and failed.")
                return HttpResponse("invalid login")
        return render(request, 'blog/login.html')


   

def ResetPassword(request):
        if request.method == 'POST':
            #email = request.POST.get('Email')
            full_name = request.POST.get('full_name')
            place = request.POST.get('Place')
            mypass = User.objects.filter(Q(full_name=full_name) & Q(place=place)).values()
            print(full_name)
            print(place)
            if mypass.filter(role='community'):
                return render(request, 'blog/AfterPassword.html')
            else:
                print("someone tried to reset and failed.")
                return HttpResponse("invalid sapir - details are not vaild")
        return render(request, 'blog/ResetPassword.html')


def AfterPassword(request):
    AfterPasswords = User.objects.filter(role = 'community')
    return render(request , 'blog/AfterPassword.html' ,{'AfterPasswords': AfterPasswords})





