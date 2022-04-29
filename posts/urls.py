from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('<slug>', views.article_page, name = "post_details"),
]