from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Blog, Comment


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


@login_required(login_url="/auth/login")
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


@login_required(login_url="/auth/login")
def my_topics(request):
    data = Blog.objects.filter(author=request.user)

    context = {"topics": data}
    return render(request, 'forum/topics.html', context=context)


def detail_topic(request, uuid):
    blog = get_object_or_404(Blog, uuid=uuid)

    if request.method == 'POST':
        content = request.POST.get('content')
        try:
            Comment.objects.create(content=content, blog=blog, author=request.user)
        except Exception as e:
            print("An error has occurred")

    context = {"blog": blog}
    return render(request, 'forum/detail_topic.html', context=context)
