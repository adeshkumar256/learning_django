from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.db.models import Avg, Max, Min


def index(request):
    # - sign for desc and remove - for asc (Ordering)
    posts = Post.objects.all().order_by("-title")
    print(posts)
    total_posts = posts.count()
    avg_rating = posts.aggregate(
        Avg("rating"), Min("rating"))  # aggregate function
    return render(request, "blogs/index.html", {
        "posts": posts,
        "total_posts": total_posts,
        "avg_rating": avg_rating
    })


def get_posts(request):
    return render(request, "blogs/posts.html")


def get_post(request, slug):
    # post = Post.objects.get(pk=slug)
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blogs/post.html", {
        "slug": slug,
        "post": post
    })
