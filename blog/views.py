from django.shortcuts import render
from app.models import Post


def base(request):
    return render(request, 'main/base.html')


def index(request):
    popular_post = Post.objects.filter(section='Popular').order_by('-id')[0:4]
    recent_post = Post.objects.filter(section='Recent').order_by('-id')[0:4]
    main_post = Post.objects.filter(Main_post=True)[0:1]

    context = {
        'popular_post': popular_post,
        'recent_post' : recent_post,
        'main_post' : main_post,
    }
    return render(request, 'main/index.html', context)