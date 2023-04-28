from django.urls import path
from . import views

urlpatterns = [
    path('myOrder/', views.myOrder, name='myOrder'),
    path('shoppingCart/', views.shoppingCart, name='shoppingCart'),
 ]