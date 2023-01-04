from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Post, User, Mission, Event
from .forms import RegisterForm, PostForm
from datetime import datetime
from django.db.models import Q
from . import forms #

def home(request):
    return render(request , 'blog/HomePage.html')
    
@login_required
def community(request):
    return render(request , 'blog/HomePageCommunity.html')

@login_required
def organization(request):
    context={'posts': Post.objects.filter(flag = '1').order_by('title'),
    'events': Event.objects.all().order_by('title')}
    return render(request , 'blog/HomePageOrganization.html', context)

@login_required
def admin(request):
    context={'posts': Post.objects.filter(flag = '1').order_by('title'),
    'events': Event.objects.all().order_by('title')}
    return render(request , 'blog/HomePageAdmin.html', context)


@login_required
def CreatEvent(request):
    formE = forms.EventForm(request.POST)
    if request.method == 'POST':
            formE.save()
            return redirect('blog-organization')
    else:
        print('invalid')
    return render(request , 'blog/CreatEvent.html',{'formE':formE})

@login_required
def CreatMission(request):
    formM = forms.MissionForm(request.POST)
    if request.method == 'POST':
            formM.save()
            return redirect('blog-admin')
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


    
def my_login(request):
        if request.method == 'POST':
            #email = request.POST.get('Email')
            full_name = request.POST.get('full_name')
            password = request.POST.get('Password')
            try:
                mydata = user.objects.get(full_name=full_name,flag='1')
            except:
                return HttpResponse("invalid login")
            if  not mydata.check_password(password):
                return HttpResponse("invalid login")
            print(full_name)
            print(password)
            login(request,mydata)
            context= {
                'money':mydata.credit,
                }
            if (mydata.role=='community'):
                return redirect('blog-community')
            if (mydata.role=='organization'):
                return redirect('blog-organization')
            if (mydata.role=='admin'):
                return redirect('blog-admin')
            else:
                print("someone tried to login and failed.")
                return HttpResponse("invalid login")
        return render(request, 'blog/login.html')


@login_required
def AllDocOrg(request):
    return render(request , 'blog/AllDocOrg.html')    

@login_required
def missions(request):
    missions =  Mission.objects.all().order_by('title')
    return render(request , 'blog/MissionPage.html' ,{'missions': missions}) 

@login_required
def AllDocAdm(request):
    return render(request , 'blog/AllDocAdm.html')    

@login_required
def ComUserPage(request):
    comuser = user.objects.filter(role = 'community').order_by('full_name')
    return render(request , 'blog/ComUserPage.html' ,{'comuser': comuser})

@login_required
def CreatPost(request):
    formP = forms.PostForm(request.POST, request.FILES)
    if request.method == 'POST':
        if formP.is_valid():
            formP.save()
            return render(request,'blog/HomePageCommunity.html')
    else:
        print('invalid')
        return render(request , 'blog/CreatPost.html',{'formP':formP})


@login_required
def OrgUserPage(request):
    orguser = user.objects.filter(Q(role = 'organization')& Q(flag = '1')).order_by('full_name')
    return render(request , 'blog/OrgUserPage.html' ,{'orguser': orguser})    


@login_required
def deleteUsers(request):
    if request.method=="POST":
        data=list(request.POST.dict().keys())[1]
        user=User.objects.get(full_name=data)
        user.delete()
        return render(request , 'blog/HomepageAdmin.html' ,{'deleteuser': (user,)})
    else:
        deleteuser = user.objects.filter(Q(role = 'organization')|Q(role = 'community')).order_by('full_name')
        return render(request , 'blog/DeleteUsers.html' ,{'deleteuser': deleteuser})  

@login_required
def UserAuth(request):
    if request.method=="POST":
        data=list(request.POST.dict().keys())[1]
        user=User.objects.get(full_name=data)
        user.flag='1'
        user.save()
        return render(request , 'blog/HomepageAdmin.html' ,{'orguser': (user,)})
    else:
        orguser = user.objects.filter((Q(role = 'organization')|Q(role = 'community'))&(Q(flag ='0'))).order_by('full_name')
        return render(request , 'blog/UserAuthorization.html' ,{'orguser': orguser})    

@login_required
def PostAuth(request):
    if request.method=="POST":
        data=list(request.POST.dict().keys())[1]
        post=Post.objects.get(title=data)
        post.flag='1'
        post.save()
        return redirect('blog-admin')
        #{'postuser': (post,)})
    else:
        postuser = Post.objects.filter(flag = '0').order_by('title')
        return render(request , 'blog/PostAuthorization.html' ,{'postuser': postuser}) 



def CreateRating(request):
    formR = forms.RatingForm(request.POST)
    if request.method == 'POST':
            formR.save()
            return redirect('blog-community')
    else:
        orguser = User.objects.filter(role = 'organization').order_by('full_name')
        return render(request , 'blog/OrgUserPage.html' ,{'orguser': orguser}) 

@login_required       
def ActivityReport(request):
    allPost =  Post.objects.all()
    allEvent = Event.objects.all()
    num_posts = Post.objects.count()
    num_events = Event.objects.count()
    return render(request , 'blog/ActivityReport.html' ,{'allPost': allPost , 'allEvent': allEvent , 'num_posts': num_posts , 'num_events':num_events})


@login_required
def addImage(request):
    formI =forms.ImageForm(request.POST, request.FILES)
    if request.method == 'POST':
        if formI.is_valid():
            formI.save()
            #return redirect('images')
            return render(request,'blog/HomePageCommunity.html')
    else:
        print('invalid')
        return render(request, 'blog/addImage.html', {'formI': formI})                      