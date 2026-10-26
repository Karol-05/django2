from django.shortcuts import get_object_or_404, render

from .models import Post


def index(request):
    posts = Post.objects.filter(status=1).order_by("-created_on")
    return render(request, "index.html", {"posts": posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=1)
    return render(request, "post_detail.html", {"post": post})