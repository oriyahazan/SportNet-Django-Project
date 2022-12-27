from django.forms import ModelForm
from .models import User
from django import forms
from . import models #


class RegisterForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['full_name','id_number','identity_qu','place','email','password','role', 'age', 'flag',
                  'credit']


class EventForm(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = ['title','content','date_posted','credit','participants']


class MissionForm(forms.ModelForm):
    class Meta:
        model = models.Mission
        fields = ['title','content']        
        