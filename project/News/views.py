from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Category, Post
from .filters import PostFilter
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm, PostDeleteForm, PostEditForm

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
    paginate_by = 10


class PostDetail(DetailView):
    model = Post
    template_name = 'News_detail.html'
    context_object_name = 'post'


class PostSearch(ListView):
    model = Post
    template_name = 'news_search.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context


#########Добавление, изменение и удаление#########


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = PostEditForm(instance=post)
    return render(request, 'edit_post.html', {'form': form, 'post': post})


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('news_list')
    return render(request, 'delete_post.html', {'post': post})
