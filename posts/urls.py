from django.urls import path

from posts.views import PostDeletView, PostUpdateView
from .views import PostListView, PostDetailView, PostCreateView


urlpatterns = [
    path('', PostListView.as_view(), name='blog_post_list'),
    path('blog_posts/<int:pk>/', PostDetailView.as_view(), name='blog_post_detail'),
    path('new_blog_post/', PostCreateView.as_view(), name='new_blog_post'),
    path('posts/<int:pk>/edit', PostUpdateView.as_view(), name='edit_blog_post'),
    path('posts/<int:pk>/delete', PostDeletView.as_view(), name='delete_blog_post'),
] 