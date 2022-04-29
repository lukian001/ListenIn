from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('<username>', views.user, name = "user_account"),
    path('login/', views.login, name = "login"),
    path('signup/', views.register, name = "signup")
]