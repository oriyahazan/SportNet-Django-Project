"""sportnet_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth import views as auth_views #
from django.urls import path, include
#from users import views as user_views
from blog import views 


urlpatterns = [

    path('admin/', admin.site.urls),
    path('register/', views.register, name='blog-register'),
    path('HomePageCommunity/', views.community, name='blog-community'),
    path('HomePageAdmin/', views.admin, name='blog-admin'),
    path('login/', views.login, name='blog-login'),
    path('HomePage/', views.home, name='blog-HomePage'),
    path('', include('blog.urls')),
    path('HomePageOrganization/' , views.organization , name='blog-organization'),
    path('CreatEvent/' , views.CreatEvent , name='blog-CreatEvent'),
    path('CreatMission/' , views.CreatMission , name='blog-CreatMission'),
    path('AllDocOrg/' , views.AllDocOrg , name='blog-AllDocOrg'),
    path('MissionPage/' , views.missions , name='blog-missions'),
    path('AllDocAdm/' , views.AllDocAdm , name='blog-AllDocAdm'),
    path('ComUserPage/' , views.ComUserPage , name='blog-ComUserPage'),
    # path('ResetPassword/' , views.ResetPassword , name='blog-ResetPassword'),
    # path('AfterPassword/' , views.AfterPassword , name='blog-AfterPassword'),
    path('CreatPost/' , views.CreatPost , name='blog-CreatPost'),
    path('OrgUserPage/' , views.OrgUserPage , name='blog-OrgUserPage'),
    path('DeleteUsers/' , views.deleteUsers , name='blog-deleteUsers'),
    path('UserAuth/' , views.UserAuth , name='blog-UserAuth'),
    path('PostAuthorization/' , views.PostAuth , name='blog-PostAuth'),
    path('ComUserPage/' , views.ComUserPage , name='blog-ComUserPage'),
    path('TrainingRating/' , views.CreateRating , name='blog-TrainingRating'),
    path('TraningDoc/' , views.CoachRating , name='blog-TraningDoc'),
    path('AllDocCom/' , views.AllDocCom , name='blog-AllDocCom'),
    
    
]
