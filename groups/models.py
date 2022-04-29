from django.db import models
from django.contrib.auth.models import Group

class GroupProfile(models.Model):
    group = models.OneToOneField(Group, on_delete = models.CASCADE)
    description = models.TextField()