from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', PostListAPIView.as_view(), name='home-api'),
    path('create/', PostCreateAPIView.as_view(), name='create-api'),
    path('detail/<str:slug>/', PostDetailAPIView.as_view(), name='detail-api'),
    path('<str:slug>/edit/', PostUpdateAPIView.as_view(), name='update-api'),
    path('<str:slug>/delete/', PostDeleteAPIView.as_view(), name='delete-api'),
]
