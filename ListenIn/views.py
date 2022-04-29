from django.shortcuts import render, redirect
from posts.models import Post

def homepage(request):
    if request.user.is_authenticated:
        posts = Post.objects.all().order_by('date')
        return render(request, 'main_page.html', {'posts' : posts})
    else:
        return redirect('accounts:login')