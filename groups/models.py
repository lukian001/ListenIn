from django.db import models
from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
from django.dispatch import receiver

class GroupProfile(models.Model):
    group = models.OneToOneField(Group, on_delete = models.CASCADE)
    owner = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
    description = models.TextField()

@receiver(post_save, sender = Group)
def create_group_profile(sender, instance, created, **kwargs):
    if created:
        GroupProfile.objects.create(group = instance)

@receiver(post_save, sender = Group)
def save_group_profile(sender, instance, **kwargs):
    instance.groupprofile.save()