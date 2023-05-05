from django.urls import path
from . import views

urlpatterns = [
    path('myOrder/', views.order,name="order"),
    path('shoppingCart/', views.shoppingCart, name='shoppingCart'),
    path('addToCart/', views.addToCart, name='addToCart'),
    path('removeCart/<int:id>',views.removeCart, name='removeCart'),
    path('checkout/', views.checkout, name='checkout'),
 ]