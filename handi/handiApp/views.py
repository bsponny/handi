from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect

from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Account

from handiApp.decorators import allowed_user_types, unauthenticated_user
from django.contrib.auth.decorators import login_required

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)

            firstName = request.POST.get('firstName')
            lastName = request.POST.get('lastName')
            hearingLevel = request.POST.get('hearingLevel')
            profilePic = request.POST.get('profilePic')
            signType = request.POST.get('signType')

            account = Account(user=user, firstName=firstName, lastName=lastName, hearingLevel=hearingLevel, signType=signType)
            account.save()
            messages.success(request, 'Account was created for ' + username)

            return redirect('handiApp:login')
        else:
            messages.error(request, 'ERROR')

    context = {'form': form}
    return render(request, 'handiApp/register.html', context)

@unauthenticated_user
def loginPage(request):
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

@login_required(login_url='handiApp:login')
def home(request):
    if request.user.account.userType == 1:
        userType = 'Student'
    elif request.user.account.userType == 2:
        userType = 'Mentor'
    elif request.user.account.userType == 3:
        userType = 'Manager'
    elif request.user.account.userType == 4:
        userType = 'Admin'
    context = {
        'userType': userType,
    }
    return render(request, 'handiApp/home.html', context)

@login_required(login_url='handiApp:login')
def learn(request):
    if request.user.account.userType == 1:
        userType = 'Student'
    elif request.user.account.userType == 2:
        userType = 'Mentor'
    elif request.user.account.userType == 3:
        userType = 'Manager'
    elif request.user.account.userType == 4:
        userType = 'Admin'
    context = {
        'userType': userType,
    }
    return render(request, 'handiApp/learn.html', context)

@login_required(login_url='handiApp:login')
def connect(request):
    if request.user.account.userType == 1:
        userType = 'Student'
    elif request.user.account.userType == 2:
        userType = 'Mentor'
    elif request.user.account.userType == 3:
        userType = 'Manager'
    elif request.user.account.userType == 4:
        userType = 'Admin'
    context = {
        'userType': userType,
    }
    return render(request, 'handiApp/connect.html', context)

@login_required(login_url='handiApp:login')
def feed(request):
    if request.user.account.userType == 1:
        userType = 'Student'
    elif request.user.account.userType == 2:
        userType = 'Mentor'
    elif request.user.account.userType == 3:
        userType = 'Manager'
    elif request.user.account.userType == 4:
        userType = 'Admin'
    context = {
        'userType': userType,
    }
    return render(request, 'handiApp/feed.html', context)

@login_required(login_url='handiApp:login')
def account(request):
    if request.user.account.userType == 1:
        userType = 'Student'
    elif request.user.account.userType == 2:
        userType = 'Mentor'
    elif request.user.account.userType == 3:
        userType = 'Manager'
    elif request.user.account.userType == 4:
        userType = 'Admin'
    context = {
        'userType': userType,
    }
    return render(request, 'handiApp/account.html', context)

@login_required(login_url='handiApp:login')
def community(request):
    if request.user.account.userType == 1:
        userType = 'Student'
    elif request.user.account.userType == 2:
        userType = 'Mentor'
    elif request.user.account.userType == 3:
        userType = 'Manager'
    elif request.user.account.userType == 4:
        userType = 'Admin'
    context = {
        'userType': userType,
    }
    return render(request, 'handiApp/community.html', context)

@login_required(login_url='handiApp:login')
def logoutUser(request):
    logout(request)
    return redirect('handiApp:login')
