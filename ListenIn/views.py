from django.http import HttpResponse

def homepage(request):
    return HttpResponse('home')

def login(request):
    return HttpResponse('login')

def register(request):
    return HttpResponse('register')