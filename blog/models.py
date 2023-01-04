from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser
# class Post(models.Model):
#     title= models.CharField(max_length=100)
#     content= models.TextField()
#     date_posted = models.DateTimeField(default=timezone.now)
#     author = models.ForeignKey(User , on_delete=models.CASCADE) #if user deleted we want to delete his post

#     def _str_(self):
#         return self.title


class user(AbstractUser): 
    full_name=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=50,unique=True)
    id_number= models.IntegerField(max_length=10,null=True)
    identity_qu=models.CharField(max_length=50,null=True)
    place = models.CharField(max_length=10,null=True)
    role = models.CharField(max_length=15,null=True)
    age = models.IntegerField(max_length=3, default=1)
    flag = models.CharField(max_length=1,default=0)
    credit = models.IntegerField(default=0)

    def _str_(self):
        return self.full_name


##############
class Event(models.Model):
    title= models.CharField(max_length=200)
    content= models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    credit = models.IntegerField(default=0)
    participants = models.IntegerField(default=0)

    def _str_(self):
        return self.title


class Mission(models.Model):
    title= models.CharField(max_length=200)
    content= models.TextField()

    def _str_(self):
        return self.title

class Post(models.Model):
    scope=models.CharField(max_length=50 , default=0)
    title= models.CharField(max_length=200)
    content= models.TextField()
    thumb=models.ImageField(default='default.png', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    credit = models.IntegerField(default=0)
    author=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    flag=models.CharField(max_length=1 , default=0)
    

    def _str_(self):
        return self.title


class Image(models.Model):
    title= models.CharField(max_length=200)
    content= models.TextField()
    image= models.ImageField(upload_to='images')

    def _str_(self):
        return self.title        


class Rating(models.Model):
    name = models.ForeignKey(user,on_delete=models.CASCADE)
    rating = models.IntegerField(default=1,max_length=10)
    good = models.CharField(max_length=2)
    
    def _str_(self):
        return str(self.name)
