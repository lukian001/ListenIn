from django.db import models

class Post(models.Model):

    slug = models.SlugField()
    text = models.TextField()
    date = models.DateField(auto_now_add = True)
    # grupul din care face parte
    # author
    # media
