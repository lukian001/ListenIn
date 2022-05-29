from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core import validators
from .models import Post, Comment
from django.contrib.auth.models import User
from posts.forms import CreatePostForm
from accounts.models import Notification
import random
import string
import mimetypes
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string


def post_page(request, slug):
    post = Post.objects.get(slug=slug)

    if post.owner is not None:
        owner = User.objects.get(id=post.owner.id)
    else:
        owner = User.objects.get(username="anonymous")

    return render(request, 'posts/post.html', {'post': post,
                                               'owner': owner})


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def create_post(request):
    if request.method == 'POST':
        post_form = CreatePostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            group = post.host_group
            post.owner = request.user

            random_str = get_random_string(16)
            check_post = Post.objects.filter(slug=random_str).exists()
            while check_post:
                random_str = get_random_string(16)
                check_post = Post.objects.filter(slug=random_str).exists()
            post.slug = random_str

            if post.media != "":
                mimetypes.init()
                mimestart = mimetypes.guess_type(post.media.url)[0]
                if mimestart is not None:
                    mimestart = mimestart.split('/')[0]

                    if mimestart == 'audio':
                        post.type = 1
                    if mimestart == 'video':
                        post.type = 2
                    if mimestart == 'image':
                        post.type = 3

            post.save()
            for user in group.user_set.all():
                if user.username != post.owner.username:
                    notification = Notification(text=post.owner.get_full_name() + " posted in " + group.name + "!",
                                                owner=user)
                    notification.save()
    return redirect('homepage')


@csrf_exempt
def post_comment(request):
    if request.user.is_authenticated:
        text = request.POST.get('comment', None)
        slug = request.POST.get('post_slug', None)
        post = Post.objects.get(slug=slug)
        comment = Comment()
        comment.owner = request.user
        comment.post = post
        comment.text = text
        comment.save()
        template = render_to_string('comments_list.html', {'comment': comment})
        return JsonResponse(template, safe=False)


@csrf_exempt
def like_post(request):
    if request.user.is_authenticated:
        slug = request.POST.get('post_slug', None)
        post = Post.objects.get(slug=slug)
        if post not in request.user.profile.liked_posts.all():
            post.likes = post.likes + 1
            request.user.profile.liked_posts.add(post)
            post.save()
        else:
            post.likes = post.likes - 1
            request.user.profile.liked_posts.remove(post)
            post.save()
        template = render_to_string('likes-date.html', {'post': post,
                                                        })
        return JsonResponse(template, safe=False)
