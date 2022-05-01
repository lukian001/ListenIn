from django.db import models
from django.contrib.auth.models import User, Group

class Post(models.Model):
    slug = models.SlugField()
    text = models.TextField()
    date = models.DateField(auto_now_add = True)
    host_group = models.ForeignKey(Group, on_delete = models.CASCADE, null = True, blank = True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
    media = models.ImageField(blank=True)

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, null = True, blank = True)
