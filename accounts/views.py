from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import CreateUserForm, CreateUserProfile


def login(request):
    return render(request, 'accounts/login.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        profile_form = CreateUserProfile(request.POST)

        user_form.fields['email'].required = True
        profile_form.fields['birthdate'].required = True

        user_form.username = request.POST['first_name'] + request.POST  ['last_name'] + str(User.objects.count())

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('homepage')
        else:
            print("Nu mere :(")
    else:
        user_form = CreateUserForm()
        profile_form = CreateUserProfile()
    return render(request, 'accounts/signup.html', {'user_form': user_form,
                                                        'profile_form': profile_form})


def user(request, username):
    if request.user.is_authenticated and request.user.username == username:
        return render(request, 'accounts/user.html', {'user': request.user})
    elif User.objects.filter(username=username).exists():
        return render(request, 'accounts/other_user.html', {'user': User.objects.get(username=username)})
    else:
        return render(request, 'error_page.html')
