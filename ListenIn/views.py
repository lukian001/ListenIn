from django.shortcuts import render, redirect
from posts.models import Post
from posts.forms import CreatePostForm


def homepage(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            posts = Post.objects.all().order_by('date')
            post_form = CreatePostForm()
            post_form.fields['host_group'].queryset = request.user.groups
            return render(request, 'main_page.html', {'posts': posts,
                                                      'post_form': post_form})
        else:
            return redirect('accounts:login')
