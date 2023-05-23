from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterationForm


def main(request):
    return render(request, 'main.html')


def register(request):
    if request.method == "POST":
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('registed'))
            return redirect('main')
    else:
        form = RegisterationForm()
        return render(request, 'register/register.html', {
            'form':form,
        })
    

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main.html')
        else:
            messages.success(request, ("login error"))
            return redirect('login')
    else:    
        return render(request, 'register/login.html', {})


def logout_view(request):
    logout(request)
    messages.success(request, ("logged out"))
    return redirect('login')