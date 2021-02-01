from django.contrib import admin
from django.urls import path

from .views import (
    CommentListAPIView,
    CommentDetailAPIView,
    CommentCreateAPIView,
    # CommentEditAPIView,
)

urlpatterns = [
    path('', CommentListAPIView.as_view(), name='list'),
    path('create/', CommentCreateAPIView.as_view(), name='create-api'),
    path('<int:pk>/', CommentDetailAPIView.as_view(), name='thread-api'),
    # path('<int:pk>/edit', CommentEditAPIView.as_view(), name='edit-api'),
    # path('<int:id>/delete/', comment_delete, name='delete'),
]
