from django.shortcuts import render
from posts.models import Post

def homepage(request):
    posts = Post.objects.all().order_by('date')
    return render(request, 'main_page.html', {'posts' : posts})