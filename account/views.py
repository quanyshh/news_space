from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.http import HttpResponseServerError

def register(request):
    try:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('account:login')  # Замените 'home' на URL вашей домашней страницы
        else:
            form = CustomUserCreationForm()
        return render(request, 'account/register.html', {'form': form})
    except Exception as e:
        return HttpResponseServerError(str(e))

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('news:HomeView')  # Замените 'home' на URL вашей домашней страницы
    else:
        form = CustomAuthenticationForm()
    return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('news:HomeView') 