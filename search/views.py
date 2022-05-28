from django.contrib.auth.models import User, Group
from django.shortcuts import render

from posts.models import Post
from search.forms import SearchForm


def search_users(text):
    text_splitted = text.split()
    users = []
    for txt in text_splitted:
        user_first_name = User.objects.filter(first_name__icontains=txt)
        user_last_name = User.objects.filter(last_name__icontains=txt)
        for user in user_first_name:
            if user not in users:
                users.append(user)
        for user in user_last_name:
            if user not in users:
                users.append(user)

    return users


def search_groups(text):
    text_splitted = text.split()
    groups = []
    for txt in text_splitted:
        groups_now = Group.objects.filter(name__icontains=txt)
        for group in groups_now:
            if group not in groups:
                groups.append(group)

    return groups


def search_posts(text):
    text_splitted = text.split()
    posts = []
    for txt in text_splitted:
        posts_now = Post.objects.filter(text__icontains=txt)
        for post in posts_now:
            if post not in posts:
                posts.append(post)

    return posts


def search(request):
    if request.method == "POST":
        search_form = SearchForm(request.POST)
        text = search_form.data['text']
        users = search_users(text)
        groups = search_groups(text)
        posts = search_posts(text)
        return render(request, 'search_result.html', {'text': text,
                                                      'users': users,
                                                      'groups': groups,
                                                      'posts': posts,
                                                      })
