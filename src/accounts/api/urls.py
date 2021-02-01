from django.contrib import admin
from django.urls import path

from .views import (
    UserCreateAPIView,
    UserLoginAPIView
)

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register-api'),
    path('login/', UserLoginAPIView.as_view(), name='login-api'),
    # path('create/', CommentCreateAPIView.as_view(), name='create-api'),
    # path('<int:pk>/', CommentDetailAPIView.as_view(), name='thread-api'),
    # path('<int:pk>/edit', CommentEditAPIView.as_view(), name='edit-api'),
    # path('<int:id>/delete/', comment_delete, name='delete'),
]
