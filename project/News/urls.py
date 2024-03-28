from django.urls import path
from .views import PostList, PostDetail, PostSearch, edit_post, create_post, delete_post
urlpatterns = [
    path('news/', PostList.as_view(), name='news_list'),
    path('news/<int:pk>/', PostDetail.as_view(), name='news_detail'),
    path('news/search/', PostSearch.as_view(), name='search_news'),
    path('news/create/', create_post, name='create_post'),
    path('news/<int:pk>/edit/', edit_post, name='edit_post'),
    path('news/<int:pk>/delete/', delete_post, name='delete_post')
]
