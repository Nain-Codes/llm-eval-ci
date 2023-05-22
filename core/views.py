from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterationForm


def main(request):
    return render(request, 'main.html')

def register(request):
    if request.method == "POST":
        user_form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        user_form=RegisterationForm()
        return render(request, 'register/register.html', {})
    

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main.html')
        else:
            messages.success(request, ("loggin error"))
            return redirect('login')
    else:    
        return render(request, 'register/login.html', {})


def logout_user(request):
    logout(request)
