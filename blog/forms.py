from django.forms import ModelForm
from .models import User
from django import forms
from . import models #

'''
class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
'''

class RegisterForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['full_name','id_number','identity_qu','place','email','password','role']
        #fields = '__all__'