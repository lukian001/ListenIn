from django.contrib.auth.models import Group, User
from django.shortcuts import render, redirect

from posts.models import Post
from .models import is_member as member
from .forms import CreateGroupForm


def create_group(request):
    if request.method == 'POST':
        create_form = CreateGroupForm(request.POST)
        if create_form.is_valid():
            group = create_form.save()
            group.groupprofile.name = group.name
            group.user_set.add(request.user)
            group.groupprofile.owner = request.user
            group.save()
            return redirect('accounts:user_account', username=request.user.username)
    else:
        create_form = CreateGroupForm()
    return render(request, 'groups/create_group.html', {'create_form': create_form})


def group_page(request, group_name):
    group = Group.objects.get(name=group_name)
    user = User.objects.get(username=request.user.username)
    is_member = member(user, group)
    posts = Post.objects.filter(host_group=group).order_by('-date')
    return render(request, 'groups/group_page.html', {'group': group,
                                                      'posts': posts,
                                                      'is_member': is_member})


def enter_group(request, group_name):
    group = Group.objects.get(name=group_name)
    group.user_set.add(User.objects.get(username=request.user.username))
    return redirect('groups:group_page', group_name=group_name)


def leave_group(request, group_name):
    group = Group.objects.get(name=group_name)
    group.user_set.remove(User.objects.get(username=request.user.username))
    return redirect('groups:group_page', group_name=group_name)
