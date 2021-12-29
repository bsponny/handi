from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect

from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
from datetime import date

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
    if request.user.account.userType == 0:
        userType = 'Student'
    elif request.user.account.userType == 1:
        userType = 'Mentor'
    elif request.user.account.userType == 2:
        userType = 'Manager'
    elif request.user.account.userType == 3:
        userType = 'Admin'
    context = {
        'userType': userType,
    }
    return render(request, 'handiApp/home.html', context)

@login_required(login_url='handiApp:login')
def learn(request):
    if request.user.account.userType == 0:
        userType = 'Student'
    elif request.user.account.userType == 1:
        userType = 'Mentor'
    elif request.user.account.userType == 2:
        userType = 'Manager'
    elif request.user.account.userType == 3:
        userType = 'Admin'
    context = {
        'userType': userType,
    }
    return render(request, 'handiApp/learn.html', context)

@login_required(login_url='handiApp:login')
def connect(request):
    if request.user.account.userType == 0:
        userType = 'Student'
    elif request.user.account.userType == 1:
        userType = 'Mentor'
    elif request.user.account.userType == 2:
        userType = 'Manager'
    elif request.user.account.userType == 3:
        userType = 'Admin'
    context = {
        'userType': userType,
    }
    return render(request, 'handiApp/connect.html', context)

@login_required(login_url='handiApp:login')
def feed(request):
    if request.user.account.userType == 0:
        userType = 'Student'
    elif request.user.account.userType == 1:
        userType = 'Mentor'
    elif request.user.account.userType == 2:
        userType = 'Manager'
    elif request.user.account.userType == 3:
        userType = 'Admin'
    context = {
        'userType': userType,
    }
    return render(request, 'handiApp/feed.html', context)

@login_required(login_url='handiApp:login')
def account(request):
    if request.method == 'POST':
        profilePic = request.POST.get('profilePic')
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        hearingLevel = request.POST.get('hearingLevel')
        signType = request.POST.get('signType')

        account = get_object_or_404(Account, user=request.user)
        account.profilePic = profilePic
        if firstName != "":
            account.firstName = firstName
        if lastName != "":
            account.lastName = lastName
        account.hearingLevel = hearingLevel
        account.signType = signType
        account.save()
        return redirect('handiApp:account')

    if request.user.account.userType == 0:
        userType = 'Student'
    elif request.user.account.userType == 1:
        userType = 'Mentor'
    elif request.user.account.userType == 2:
        userType = 'Manager'
    elif request.user.account.userType == 3:
        userType = 'Admin'
    context = {
        'profilePic': request.user.account.profilePic,
        'userType': userType,
        'firstName': request.user.account.firstName,
        'lastName': request.user.account.lastName,
        'hearingLevel': request.user.account.hearingLevel,
        'signType': request.user.account.signType,
    }
    return render(request, 'handiApp/account.html', context)

@login_required(login_url='handiApp:login')
def mentorRequest(request):
    if request.method == "POST":
        requestDate = date.today()
        mentorRequest = MentorRequest(requestor=request.user, requestDate=requestDate)
        mentorRequest.save()
        messages.success(request, f"Successfully submitted request")

    context = {
    }
    return render(request, 'handiApp/mentorRequest.html', context)

@login_required(login_url='handiApp:login')
def mentorRequests(request):
    messages = []

    if request.method == 'POST':
        mentorRequest = get_object_or_404(MentorRequest, pk=request.POST.get('id'))
        mentorAccount = get_object_or_404(Account, user=mentorRequest.requestor)
        status = request.POST.get('status')
        if (status == 'approve'):
            mentorAccount.userType = 1
            mentorAccount.save()

            messages.append(f"Request was approved and {mentorAccount.user.username} is now a Mentor")
        else:
            messages.append(f"Request was denied and {mentorAccount.user.username} is still a student")
        mentorRequest.delete()

    requests = MentorRequest.objects.all()
    requests = requests.order_by('requestDate')
    if requests.count() == 0:
        messages.append("There are currently no mentor requests")

    context = {'requests': requests, 'messages': messages}
    return render(request, 'handiApp/mentorRequests.html', context)

@login_required(login_url='handiApp:login')
def request(request, request_id):
    try:
        mentorRequest = MentorRequest.objects.get(pk=request_id)
    except MentorRequest.DoesNotExist:
        raise Http404("Request does not exist")

    context={
            'mentorRequest': mentorRequest,
    }

    return render(request, 'handiApp/request.html', context)

@login_required(login_url='handiApp:login')
def userType(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        userType = request.POST.get('userType')
        user = get_object_or_404(User, username=username)
        account = get_object_or_404(Account, user=user)
        account.userType = userType
        account.save()

    accounts = Account.objects.order_by('user').exclude(userType=3)
    context = {
            'accounts': accounts,
    }
    return render(request, 'handiApp/userType.html', context)

@login_required(login_url='handiApp:login')
def community(request):
    if request.user.account.userType == 0:
        userType = 'Student'
    elif request.user.account.userType == 1:
        userType = 'Mentor'
    elif request.user.account.userType == 2:
        userType = 'Manager'
    elif request.user.account.userType == 3:
        userType = 'Admin'
    context = {
        'userType': userType,
    }
    return render(request, 'handiApp/community.html', context)

@login_required(login_url='handiApp:login')
def logoutUser(request):
    logout(request)
    return redirect('handiApp:login')
