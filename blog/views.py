from django.shortcuts import render
from blog.models import Post, Comment, Category


# Create your views here.
def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
