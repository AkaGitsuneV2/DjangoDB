from django.contrib.auth.models import User, Group
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        # Рассчитываем суммарный рейтинг каждой статьи автора умноженный на 3
        post_rating = sum(post.rating for post in self.post_set.all()) * 3

        # Рассчитываем суммарный рейтинг всех комментариев автора
        comment_rating = sum(comment.rating for comment in self.comment_set.all())

        # Рассчитываем суммарный рейтинг всех комментариев к статьям автора
        comment_to_posts_rating = sum(
            comment.rating for post in self.post_set.all() for comment in post.comment_set.all())

        # Обновляем рейтинг автора
        self.rating = post_rating + comment_rating + comment_to_posts_rating
        self.save()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    POST_TYPES = [
        ('article', 'Статья'),
        ('news', 'Новость')
    ]
    post_type = models.CharField(max_length=7, choices=POST_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.IntegerField(default=0)

    def preview(self):
        return self.content[:124] + '...' if len(self.content) > 124 else self.content

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class CommentCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


@receiver(post_save, sender=User)
def add_user_to_common(sender, instance, created, **kwargs):
    if created:
        common_group = Group.objects.get(name='common')
        instance.groups.add(common_group)


class AuthorRequest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    message = models.TextField()
    processed = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Запрос стать автором от {self.user.username}"
