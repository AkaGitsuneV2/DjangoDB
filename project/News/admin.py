from django.contrib import admin
from .models import CommentCategory, Author, Post, PostCategory, Category, AuthorRequest
from django.contrib.auth.models import Group

admin.site.register(CommentCategory)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Category)


@admin.register(AuthorRequest)
class AuthorRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'processed', 'approved']
    list_filter = ['processed', 'approved']
    search_fields = ['user__username']

    def save_model(self, request, obj, form, change):
        if obj.approved and not obj.processed:
            group = Group.objects.get(name='author')
            obj.user.groups.add(group)
            obj.processed = True
        obj.save()
