from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

class DateInput(forms.DateInput):
    input_type = 'date'

class CreateUserProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birthdate']
        widgets = {
            'birthdate' : DateInput()
        }