from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name='list'),
    path('userlist/', views.userList, name='userList'),
    path('dashboard/', views.dashboard, name='dashboard'),    
]