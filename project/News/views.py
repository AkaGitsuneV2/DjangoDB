from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Post

# Create your views here.


class CategoryList(ListView):
    model = Category
    ordering = 'name'
    template_name = 'CategoryList.html'
    context_object_name = 'Category'


class PostList(ListView):
    model = Post
    ordering = '-created_at'
    template_name = 'News.html'
    context_object_name = 'news'


class PostDetail(DetailView):
    model = Post
    template_name = 'News_detail.html'
    context_object_name = 'post'
