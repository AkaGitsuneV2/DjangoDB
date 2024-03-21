from django.urls import path
from .views import PostList, PostDetail
urlpatterns = [
    path('news/', PostList.as_view(), name='news_list'),
    path('news/<int:pk>/', PostDetail.as_view(), name='news_detail')
]
