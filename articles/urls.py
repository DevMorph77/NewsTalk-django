from django.urls import path
from .views import (
    ArticleListView, ArticleCreateView, ArticleDetailView, 
    ArticleUpdateView, ArticleDeleteView, CommentUpdateView, CommentDeleteView
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('article/new/', ArticleCreateView.as_view(), name='article_new'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]
