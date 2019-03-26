from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from clients.forms import UserLoginForm
from expenses.views import dashboard


# Create your views here.
@csrf_exempt
def usersignup(request):
    if request.user.username:
        return redirect(dashboard)
    message = ''
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = User()
            user.username = username
            user.set_password(password)
            user.save()
            message = 'User registered successfully, please click to login'
    return render(request, 'signup.html', {'form': form, 'msg': message})


def userlogin(request):
    if request.user.username:
        return redirect(dashboard)
    form = UserLoginForm()
    message = ''
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,
                                password=password)
            if user is None:
                message = 'Invalid User'
            else:
                login(request, user)
                return redirect(dashboard)
    return render(request, 'login.html', {'form': form, 'msg': message})


def userlogout(request):
    logout(request)
    return redirect(usersignup)