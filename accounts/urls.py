from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('<username>', views.user_view, name = "user_account"),
    path('login/', views.login_view, name = "login"),
    path('signup/', views.register_view, name = "signup"),
    path('logout/', views.logout_view, name = "logout")
]