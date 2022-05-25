from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('create-group/', views.create_group, name="create_group"),
    path('<group_name>', views.group_page, name="group_page"),
    path('<group_name>/enter_group/', views.enter_group, name="enter_group"),
    path('<group_name>/leave_group/', views.leave_group, name="leave_group")
]
