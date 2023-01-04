from django.forms import ModelForm
from .models import user
from django import forms
from . import models #


class RegisterForm(forms.ModelForm):
    class Meta:
        model = models.user
        fields = ['username','full_name','id_number','identity_qu','place','email','password','role', 'age' ]


class EventForm(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = ['title','content','date_posted','credit','participants']


class MissionForm(forms.ModelForm):
    class Meta:
        model = models.Mission
        fields = ['title','content']  

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['scope','title','content','thumb','date_posted','credit','author'] 

class RatingForm(forms.ModelForm):
    class Meta:
        model = models.Rating
        fields = ['name', 'rating', 'good'] 

        fields = ['scope','title','content','thumb','date_posted','credit']  

class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = ['title','content','image']                      
        