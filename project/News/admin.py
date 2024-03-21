from django.contrib import admin
from .models import CommentCategory, Author, Post, PostCategory, Category

admin.site.register(CommentCategory)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Category)

