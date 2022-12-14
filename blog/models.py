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
    id_number= models.CharField(max_length=10)
    identity_qu=models.CharField(max_length=50)
    place = models.CharField(max_length=10)
    role = models.CharField(max_length=15)
    email= models.EmailField(max_length=40)
    password = models.CharField(max_length=20)


    def __str__(self):
        return self.full_name + ',' + self.id_number + ',' + self.identity_qu  + ','+self.place+ ','+ self.role +',' + self.email + ',' + self.password
        

