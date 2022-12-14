from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, User
from .forms import RegisterForm
from datetime import datetime
from django.db.models import Q
from . import forms #

def home(request):
    context= {
        'posts' : Post.objects.all()
    }
    return render(request , 'blog/HomePage.html' , context)

def posts(request):
    posts =  Post.objects.all().order_by('title')
    return render(request , 'blog/posts_page.html' ,{'posts': posts})

    

def about(request):
    return HttpResponse('<h1>Blog About</h1>')

'''
def register(request):
    form=RegisterForm()
    if request.method == 'POST':
        email=request.POST.get('email')
        id=request.POST.get('id_number')
        role= request.POST.get('role')
        form = RegisterForm(request.POST)
        #mydata = ValidId.objects.filter(Q(role=role) & Q(id_number=id)).valuse()
        mydataUnique = User.objects.filter(Q(email=email) | Q(id_number=id)).values()
        if len(mydataUnique) == 0: #and mydata:
            if form.is_valid():
                form.save()
                return render(request,'blog/register.html' )  #add html page
            else:
                return HttpResponse("Invalid login detelis supplied.")
        else:
            return HttpResponse("Invalid login detelis supplied")   


    context = {'form':form}
    return render(request , 'blog/register.html' , context)   ##add html page

'''



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
            email = request.POST.get('email')
            password = request.POST.get('password')
            mydata = User.objects.filter(Q(email=email) & Q(password=password)).values()
            if mydata.filter(role='community'):
                
            if mydata.filter(role='community'):
