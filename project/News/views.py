from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Category, Post, UserProfile, AuthorRequest
from .filters import PostFilter
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm, PostDeleteForm, PostEditForm, AuthorRequestForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.





class CategoryList(ListView):
    model = Category
    ordering = 'name'
    template_name = 'CategoryList.html'
    context_object_name = 'Category'


class UserUpdate(UpdateView):
    model = UserProfile
    fields = ['login', 'password']
    template_name = 'user_profile.html'
    success_url = '/profile/'

    def get_object(self, queryset=None):
        # Получаем текущего пользователя
        return self.request.user

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

class AddPost(PermissionRequiredMixin, CreateView):
    model = Post
    fields = ['author', 'post_type', 'categories', 'title', 'content']
    template_name = 'create_post.html'
    success_url = '/news/create/'
    permission_required = 'post.add_post'


class UpdatePost(PermissionRequiredMixin, UpdateView):
    model = Post
    fields = ['author', 'post_type', 'categories', 'title', 'content']
    template_name = 'edit_post.html'
    success_url = '/news/edit/'
    permission_required = 'post.change_post'


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


@login_required
def news_list(request):
    if not request.user.groups.filter(name='author').exists() and not AuthorRequest.objects.filter(
            user=request.user).exists():
        if request.method == 'POST':
            form = AuthorRequestForm(request.POST)
            if form.is_valid():
                request_obj = form.save(commit=False)
                request_obj.user = request.user
                request_obj.save()
                return redirect('profile')
            else:
                form = AuthorRequestForm()
            return render(request, 'request_author.html', {'form': form})
        else:
            return redirect('profile')