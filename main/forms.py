from django import forms
from .models import Addblog
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Addblog
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']