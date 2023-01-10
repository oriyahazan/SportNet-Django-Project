from django.forms import ModelForm
from .models import user
from django import forms
from . import models #
from django.utils import timezone



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
        fields = ['scope','title','content','thumb','date_posted','credit']

class RatingForm(forms.ModelForm):
    class Meta:
        model = models.Rating
        fields = ['name', 'rating', 'good']  

class ImageForm(forms.Form):
    image = forms.ImageField()
    title= forms.CharField(max_length=200, required=True)
    content= forms.CharField(required=True)
    class Meta:
        model = models.Image
        fields = ['title','content','image'] 

class CreateGuideForm(forms.ModelForm):
    class Meta:
        model = models.CreateGuide
        fields = ['title','context']


class DonateForm(forms.ModelForm):
    class Meta:
        model = models.Donate
        fields = ['friend', 'cost']                              
        
