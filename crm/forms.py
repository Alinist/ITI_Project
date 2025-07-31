from django import forms
from .models import Record
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields =['first_name', 'last_name', 'phone', 'category', 'height', 'weight', 'address']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'phone', 'category', 'height', 'weight', 'address']