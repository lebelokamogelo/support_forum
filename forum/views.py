from django.shortcuts import render
from .models import Blog

def index(request):
    context = {
        "blog": Blog.objects.all()
    }
    return render(request, 'forum/index.html', context=context)
