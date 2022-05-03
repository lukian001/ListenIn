from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('create-group/', views.create_group, name="create_group"),
    path('<group_name>', views.group_page, name="group_page"),
]
