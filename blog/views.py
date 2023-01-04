from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, user, Mission, Event, Rating, Image, RatingForm
from datetime import datetime
from django.db.models import Q
from .forms import ImageForm
from . import forms
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required


def log_out(request):
    logout(request)
    return redirect('blog-login')

def home(request):
    return render(request , 'blog/HomePage.html')
    
@login_required
def community(request):
    if request.method =="POST":
        key=list(request.POST.dict().keys())[1]
        post=Post.objects.get(id=key)
        user=request.user
        user.credit-=post.credit
        author = post.author
        author.credit+=post.credit
        #registpost.author
        user.save()
        author.save()
    context={'posts': Post.objects.filter(flag = '1').order_by('title'),
    'money':request.user.credit,
    'events': Event.objects.all().order_by('title')}
    return render(request, 'blog/HomePageCommunity.html',context)

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
            return render(request,'blog/HomePageOrganization.html')
    else:
        print('invalid')
    return render(request , 'blog/CreatEvent.html',{'formE':formE})

@login_required
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
        age = int(request.POST.get('age'))
        place = str(request.POST.get('place'))
        if age > 17 and place == 'ישראל':
            user1=form.save()
            user1.set_password(request.POST.dict()['password'])
            user1.save()
            return render(request,'blog/HomePage.html')
        else:
            return HttpResponse('sorry but your age is under 18 you are not from israel')
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
            x=formP.save()
            x.author=request.user
            x.save()
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
        user1=user.objects.get(full_name=data)
        user1.delete()
        return render(request , 'blog/HomepageAdmin.html' ,{'deleteuser': (user1,)})
    else:
        deleteuser = user.objects.filter(Q(role = 'organization')|Q(role = 'community')).order_by('full_name')
        return render(request , 'blog/DeleteUsers.html' ,{'deleteuser': deleteuser})  

@login_required
def UserAuth(request):
    if request.method=="POST":
        data=list(request.POST.dict().keys())[1]
        user1=user.objects.get(full_name=data)
        user1.flag='1'
        user1.save()
        return render(request , 'blog/HomepageAdmin.html' ,{'orguser': (user1,)})
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
        return render(request , 'blog/HomepageAdmin.html' ,{'postuser': (post,)})
    else:
        orguser = user.objects.filter(role = 'organization').order_by('full_name')
        return render(request , 'blog/OrgUserPage.html' ,{'orguser': orguser}) 



def CreateRating(request):
    formR = forms.RatingForm(request.POST)
    if request.method == 'POST':
            formR.save()
            return render(request,'blog/HomePageCommunity.html')
    else:
        print('invalid')
        return render(request , 'blog/TrainingRating.html', {'formR':formR})   


        
def ActivityReport(request):
    allPost =  Post.objects.all()
    allEvent = Event.objects.all()
    num_posts = Post.objects.count()
    num_events = Event.objects.count()
    return render(request , 'blog/ActivityReport.html' ,{'allPost': allPost , 'allEvent': allEvent , 'num_posts': num_posts , 'num_events':num_events})

                


def AllDocCom(request):
    return render(request , 'blog/AllDocCom.html')   

def CoachRating(request):
    Couch = Rating.objects.all().order_by('name')
    return render(request , 'blog/TraningDoc.html',{'Couch': Couch}) 

