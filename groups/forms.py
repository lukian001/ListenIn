from django import forms
from . import models


class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = models.Group
        fields = ['name']