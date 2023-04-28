from django.shortcuts import render
# Create your views here.
def myOrder(request):
    return render(request, 'myOrder.html')

def shoppingCart(request):
    return render(request,'shoppingCart.html')
