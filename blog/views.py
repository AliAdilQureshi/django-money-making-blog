from django.shortcuts import render
from app.models import Post


def base(request):
    return render(request, 'main/base.html')


def index(request):
    popular_post = Post.objects.filter(section='Popular').order_by('-id')[0:4]
    recent_post = Post.objects.filter(section='Recent').order_by('-id')[0:4]
    main_post = Post.objects.filter(Main_post=True)[0:1]
    Editors_Pick = Post.objects.filter(section='Editors_Pick').order_by('-id')
    Trending = Post.objects.filter(section='Trending').order_by('-id')


    context = {
        'popular_post': popular_post,
        'recent_post' : recent_post,
        'main_post' : main_post,
        'Editors_Pick' : Editors_Pick,
        'Trending' : Trending,
    }
    return render(request, 'main/index.html', context)