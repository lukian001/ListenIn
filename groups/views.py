from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from .forms import CreateGroupForm


def create_group(request):
    if request.method == 'POST':
        create_form = CreateGroupForm(request.POST)
        if create_form.is_valid():
            group = create_form.save()
            group.groupprofile.name=group.name
            group.user_set.add(request.user)
            return redirect('groups:group_page', group_name=group.name)
    else:
        create_form = CreateGroupForm()
    return render(request, 'groups/create_group.html', {'create_form': create_form})


def group_page(request, group_name):
    group = Group.objects.get(name=group_name)
    return render(request, 'groups/group_page.html', {'group': group})
