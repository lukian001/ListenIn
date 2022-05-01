from django import forms
from . import models


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['host_group', 'text', 'media']