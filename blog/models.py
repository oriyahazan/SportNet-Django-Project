from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title= models.CharField(max_length=100)
    content= models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User , on_delete=models.CASCADE) #if user deleted we want to delete his post

    def __str__(self):
        return self.title


class User(models.Model): 
    full_name = models.CharField(max_length=30)
    id_number= models.IntegerField(max_length=10)
    identity_qu=models.CharField(max_length=50)
    place = models.CharField(max_length=10)
    role = models.CharField(max_length=15)
    email= models.EmailField(max_length=40)
    password = models.CharField(max_length=20)
    age = models.IntegerField(max_length=3)
    flag = models.CharField(max_length=1)
    credit = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name


##############
class Event(models.Model):
    title= models.CharField(max_length=200)
    content= models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    credit = models.IntegerField(default=0)
    participants = models.IntegerField()

    def __str__(self):
        return self.title


class Mission(models.Model):
    title= models.CharField(max_length=200)
    content= models.TextField()

    def __str__(self):
        return self.title

