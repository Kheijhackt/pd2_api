from django.urls import path
from .views import create_user, user

urlpatterns = [
    path('create_user/', create_user),
    path('user/<str:pk>/', user),
]