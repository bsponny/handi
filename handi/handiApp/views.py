from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect

from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Account

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('handiApp:home')
        else:
            messages.info(request, 'Username or password is incorrect.')

    return render(request, 'handiApp/login.html', {})

def home(request):
    return render(request, 'handiApp/home.html', {})
