from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    if request.mthod == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeatPassword = request.POST['repeatPassword']

        if password == repeatPassword:
            pass
        else:
            error_message = 'Password do not match'
            return render(request, 'signup.html', {'error_message':error_message})


    return render(request, 'signup.html')

def logout(request):
    return render(request, 'logout.html')