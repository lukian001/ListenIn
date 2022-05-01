from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('<slug>', views.article_page, name = "post_details"),
    path('create_post', views.create_post, name = "create_post"),
]