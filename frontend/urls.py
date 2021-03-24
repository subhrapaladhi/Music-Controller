from django.urls import path, include
from .views import index
urlpatterns = [
    path('', index),
    path('join/', index),
    path('join/1', index),
    path('create/', index)
]
