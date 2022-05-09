from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.models import User
from posts.forms import CreatePostForm


def post_page(request, slug):
    post = Post.objects.get(slug=slug)

    if post.owner is not None:
        owner = User.objects.get(id=post.owner.id)
    else:
        owner = User.objects.get(username="anonymous")

    return render(request, 'posts/post.html', {'post': post,
                                               'owner': owner})


def create_post(request):
    if request.method == 'POST':
        post_form = CreatePostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.owner = request.user
            post.save()
    return redirect('homepage')
