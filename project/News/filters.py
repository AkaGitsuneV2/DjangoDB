import django_filters
from django_filters import DateFromToRangeFilter
from django_filters.widgets import RangeWidget

from .models import Post
from django.forms import DateInput


class PostFilter(django_filters.FilterSet):

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'author__user__username': ['icontains'],
            'created_at': ['gte']
        }

