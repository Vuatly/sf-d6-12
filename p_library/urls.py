from django.contrib import admin  
from django.urls import path  
from .views import friend_info
  

app_name = 'p_library'  
urlpatterns = [  
    path('friends', friend_info, name='friend_list'),
]