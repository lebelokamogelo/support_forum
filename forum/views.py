from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect, reverse

from .forms import UserForm
from .models import Blog


def index(request):
    context = {
        "blog": Blog.objects.all()
    }
    return render(request, 'forum/index.html', context=context)


def search(request):
    query = request.GET.get('q')
    queryset = Blog.objects.all()
    if query:
        filter = Q(title__icontains=query) | Q(description__icontains=query)
        queryset = Blog.objects.filter(filter)

    context = {
        'blog': queryset
    }

    return render(request, 'forum/search.html', context=context)


@login_required(login_url="/login")
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title and description:
            Blog.objects.create(title=title,
                                description=description,
                                author=request.user)
            context = {
                "success": "Your post was created successfully"
            }
            return render(request, 'forum/create.html', context=context)

        context = {
            "error": "All fields are required"
        }

        return render(request, 'forum/create.html', context=context)
    return render(request, 'forum/create.html')


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
            return render(request, 'forum/auth/login.html',
                          context={"error": error})

    return render(request, 'forum/auth/login.html')


def create_account(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pasword')

        if not username and not password:
            error = "All fields are required"
            return render(request, 'forum/auth/create.account.html',
                          context={"error": error})

        if User.objects.filter(username=username.lower()).exists:
            error = "Username already in use"
            return render(request, 'forum/auth/create.account.html',
                          context={"error": error})

        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('login'))

    return render(request, 'forum/auth/create.account.html')


def logout_(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))

    logout(request)
    return render(request, 'forum/auth/login.html')
