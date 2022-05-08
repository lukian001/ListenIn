from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from .forms import CreateUserForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST':
        user_form = AuthenticationForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.get_user()
            login(request, user)
            return redirect('homepage')
    else:
        signup_form = CreateUserForm()
        user_form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'user_form': user_form,
                                                   'signup_form': signup_form})


def register_view(request):
    if request.method == 'POST':
        signup_form = CreateUserForm(request.POST)

        signup_form.fields['email'].required = True

        if signup_form.is_valid():
            user = signup_form.save()
            login(request, user)
            return redirect('accounts:user_account', user.username)
        else:
            user_form = AuthenticationForm()
            return render(request, 'accounts/login.html', {'user_form': user_form,
                                                           'signup_form': signup_form})
    return redirect('accounts:login')


def user_view(request, username):
    if request.user.is_authenticated and request.user.username == username:
        return render(request, 'accounts/user.html', {'user': request.user})
    elif User.objects.filter(username=username).exists():
        return render(request, 'accounts/other_user.html', {'user': User.objects.get(username=username)})
    else:
        return render(request, 'error_page.html')


def logout_view(request):
    logout(request)
    return redirect('accounts:login')
