from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# class Post(models.Model):
#     title= models.CharField(max_length=100)
#     content= models.TextField()
#     date_posted = models.DateTimeField(default=timezone.now)
#     author = models.ForeignKey(User , on_delete=models.CASCADE) #if user deleted we want to delete his post

#     def __str__(self):
#         return self.title


class User(models.Model): 
    full_name = models.CharField(max_length=30)
    id_number= models.IntegerField(max_length=10)
    identity_qu=models.CharField(max_length=50)
    place = models.CharField(max_length=10)
    role = models.CharField(max_length=15)
    email= models.EmailField(max_length=40)
    password = models.CharField(max_length=20)
    age = models.IntegerField(max_length=3, default=1)
    flag = models.CharField(max_length=1,default=0)
    credit = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name


##############
class Event(models.Model):
    title= models.CharField(max_length=200)
    content= models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    credit = models.IntegerField(default=0)
    participants = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Mission(models.Model):
    title= models.CharField(max_length=200)
    content= models.TextField()

    def __str__(self):
        return self.title

class Post(models.Model):
    scope=models.CharField(max_length=50 , default=0)
    title= models.CharField(max_length=200)
    content= models.TextField()
    thumb=models.ImageField(default='default.png', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    credit = models.IntegerField(default=0)
    author=models.CharField(max_length=50 , default=0)
    flag=models.CharField(max_length=1 , default=0)

    def _str_(self):
        return self.title


class Rating(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField(default=1,max_length=10)
    good = models.CharField(max_length=2)
    
    def __str__(self):
        return str(self.name)


