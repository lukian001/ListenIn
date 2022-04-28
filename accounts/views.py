from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def login(request):
    return HttpResponse('login')

def register(request):
    form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form' : form})

def user(request, username):
    if request.user.is_authenticated and request.user.username == username:
        return render(request, 'accounts/user.html', #
                      {'lastname' : request.user.last_name, #
                       'firstname' : request.user.first_name})
    else:
        return render(request, 'error_page.html')