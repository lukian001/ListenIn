from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('<username>', views.user),
    path('login/', views.login),
    path('signup/', views.register),
]