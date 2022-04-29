from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = "main"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('post/', include('posts.urls')),
    path('', views.homepage, name = "homepage"),
]

urlpatterns += staticfiles_urlpatterns()