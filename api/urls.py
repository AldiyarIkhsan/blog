from django.urls import path
from .models import Post, Comment, Category
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users//', views.UserDetail.as_view()),
    path('posts/', views.PostList.as_view()),
    path('posts//', views.PostDetail.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('comments//', views.CommentDetail.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories//', views.CategoryDetail.as_view()),
]