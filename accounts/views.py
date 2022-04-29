from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def login(request):
   return render(request, 'accounts/login.html')

def register(request):
    form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form' : form})

def user(request, username):
    if request.user.is_authenticated and request.user.username == username:
        return render(request, 'accounts/user.html', {'user' : request.user})
    elif User.objects.filter(username = username).exists():
        return render(request, 'accounts/other_user.html', {'user' : User.objects.get(username = username)})
    else:
        return render(request, 'error_page.html')