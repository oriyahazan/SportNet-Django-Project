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
            try:
                mydata = User.objects.get(full_name=full_name, password=password,flag='1')
            except:
                return HttpResponse("invalid login")
            print(full_name)
            print(password)
            if (mydata.role=='community'):
                return render(request, 'blog/HomePageCommunity.html')
            if (mydata.role=='organization'):
                return render(request, 'blog/HomePageOrganization.html')
            if (mydata.role=='admin'):
                return render(request, 'blog/HomePageAdmin.html')
            else:
                print("someone tried to login and failed.")
                return HttpResponse("invalid login")
        return render(request, 'blog/login.html')

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


def CreatPost(request):
    formP = forms.PostForm(request.POST, request.FILES)
    if request.method == 'POST':
        if formP.is_valid():
            formP.save()
            return render(request,'blog/HomePageCommunity.html')
    else:
        print('invalid')
    return render(request , 'blog/CreatPost.html',{'formP':formP})


def OrgUserPage(request):
    # if request.method=="POST":
    #     data=list(request.POST.dict().keys())[1]
    #     user=User.objects.get(full_name=data)
    #     user.flag='1'
    #     user.save()
    #     return render(request , 'blog/OrgUserPage.html' ,{'orguser': (user,)})
    # else:
    orguser = User.objects.filter(role = 'organization').order_by('full_name')
    return render(request , 'blog/OrgUserPage.html' ,{'orguser': orguser})    


def deleteUsers(request):
    if request.method=="POST":
        data=list(request.POST.dict().keys())[1]
        user=User.objects.get(full_name=data)
        user.delete()
        return render(request , 'blog/HomepageAdmin.html' ,{'deleteuser': (user,)})
    else:
        deleteuser = User.objects.filter(Q(role = 'organization')|Q(role = 'community')).order_by('full_name')
        return render(request , 'blog/DeleteUsers.html' ,{'deleteuser': deleteuser})  

def UserAuth(request):
    if request.method=="POST":
        data=list(request.POST.dict().keys())[1]
        user=User.objects.get(full_name=data)
        user.flag='1'
        user.save()
        return render(request , 'blog/HomepageAdmin.html' ,{'orguser': (user,)})
    else:
        orguser = User.objects.filter((Q(role = 'organization')|Q(role = 'community'))&(Q(flag ='0'))).order_by('full_name')
        return render(request , 'blog/UserAuthorization.html' ,{'orguser': orguser})    

def PostAuth(request):
    if request.method=="POST":
        data=list(request.POST.dict().keys())[1]
        post=Post.objects.get(title=data)
        post.flag='1'
        post.save()
        return render(request , 'blog/HomepageAdmin.html' ,{'postuser': (post,)})
    else:
        postuser = Post.objects.filter(flag = '0').order_by('title')
        return render(request , 'blog/PostAuthorization.html' ,{'postuser': postuser})

    
