from django.urls import path
from .views import register_device, device

urlpatterns = [
    path('register_device/', register_device),
    path('device/<str:pk>/', device),
]