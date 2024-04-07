from django import forms
from .models import Post, AuthorRequest


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'post_type', 'categories', 'title', 'content']


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'post_type', 'categories', 'title', 'content']


class PostDeleteForm(forms.Form):
    pass


class AuthorRequestForm(forms.ModelForm):
    class Meta:
        model = AuthorRequest
        fields = ['message']