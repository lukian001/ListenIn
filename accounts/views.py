from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from posts.models import Post
from groups.forms import CreateGroupForm
from .models import FriendRequest

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
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
        is_friend = user.groups.filter(name=str(request.user.id) + request.user.username + str(request.user.id)).exists()
        request_sent = FriendRequest.objects.filter(user_from=request.user, user_to=user).exists() or FriendRequest.objects.filter(user_from=user, user_to=request.user).exists()
        group_form = CreateGroupForm()
        return render(request, 'accounts/user.html', {'user': user,
                                                      'group_form': group_form,
                                                      'posts': Post.objects.filter(owner=user),
                                                      'is_friend': is_friend,
                                                      'request_sent': request_sent})
    else:
        return render(request, 'error_page.html')


def logout_view(request):
    logout(request)
    return redirect('accounts:login')


def add_friend(request, user_to_username):
    if request.method == 'POST':
        user_to = User.objects.get(username=user_to_username)
        friend_request = FriendRequest(user_from=request.user, user_to=user_to)
        friend_request.save()
    return redirect('accounts:user_account', username=user_to_username)
