from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    text = models.TextField()
    date = models.DateField(auto_now_add = True)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    # imageUrl =
    description = models.TextField()