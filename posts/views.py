from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User

def article_page(request, slug):
    post = Post.objects.get(slug = slug)

    if post.owner is not None:
        owner = User.objects.get(id = post.owner.id)
    else:
        owner = User.objects.get(username = "anonymous")

    return render(request, 'posts/post.html', {'post' : post, #
                                               'owner' : owner})