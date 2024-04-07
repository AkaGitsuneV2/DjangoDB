from django.urls import path
from django.contrib.auth.views import LoginView
from .views import PostList, PostDetail, PostSearch, edit_post, create_post, delete_post, UserUpdate, news_list
from allauth.account.views import SignupView
urlpatterns = [
    path('news/', PostList.as_view(), name='news_list'),
    path('news/<int:pk>/', PostDetail.as_view(), name='news_detail'),
    path('news/search/', PostSearch.as_view(), name='search_news'),
    path('news/create/', create_post, name='create_post'),
    path('news/<int:pk>/edit/', edit_post, name='edit_post'),
    path('news/<int:pk>/delete/', delete_post, name='delete_post'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/', UserUpdate.as_view(), name='profile'),
    path('become_author/', news_list, name='home')
]
