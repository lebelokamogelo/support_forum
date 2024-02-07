from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse

from accounts.forms import UserForm


def login_(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse('home'))
        else:
            error = "Username or password is incorrect"
            return render(request, 'login.html',
                          context={"error": error})

    return render(request, 'login.html')


def create_account(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pasword')

        if not username and not password:
            error = "All fields are required"
            return render(request, 'create.account.html',
                          context={"error": error})

        if User.objects.filter(username=username.lower()).exists:
            error = "Username already in use"
            return render(request, 'create.account.html',
                          context={"error": error})

        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('login'))

    return render(request, 'create.account.html')


def logout_(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))

    logout(request)
    return render(request, 'login.html')
