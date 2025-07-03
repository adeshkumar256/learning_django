from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "blogs/index.html")


def get_posts(request):
    return render(request, "blogs/posts.html")


def get_post(request, slug):
    return render(request, "blogs/post.html", {
        "slug": slug
    })
