import os
import django

# Устанавливаем переменную окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.project.settings')

# Инициализируем настройки Django
django.setup()
from django.contrib.auth.models import User
from News.models import Author, Category, Post, CommentCategory

