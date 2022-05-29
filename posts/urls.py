from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('<slug>', views.post_page, name="post_details"),
    path('create_post/', views.create_post, name="create_post"),
    path('comment/', views.post_comment, name="post_comment"),
    path('like/', views.like_post, name="like_post"),

]
