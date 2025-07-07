from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


def index(request):
    posts = Post.objects.filter()
    return render(request, "blogs/index.html", {
        "posts": posts
    })


def get_posts(request):
    return render(request, "blogs/posts.html")


def get_post(request, slug):
    # post = Post.objects.get(pk=slug)
    post = get_object_or_404(Post, pk=slug)
    return render(request, "blogs/post.html", {
        "slug": slug,
        "post": post
    })
