from re import A
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def UserRegister(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(
                cd['username'], cd['email'], cd['password'],)
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.save()
            messages.success(request, 'User Register Successfully', 'success')
            return redirect('Home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def UserLogin(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(
                    request, 'User logged Successfully', 'success')
                return redirect('Home')
            else:
                messages.error(
                    request, 'username or password is wrong', 'danger')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def UserLogout(request):
    logout(request)
    messages.success(
        request, 'User logout Successfully', 'success')
    return redirect('Home')
