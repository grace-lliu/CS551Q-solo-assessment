from django.shortcuts import render
from order.models import Order
from parse_data.models import Product
from user_admin.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import plotly.graph_objs as go
from plotly.offline import plot

def is_admin(request):
    user_id = request.COOKIES.get('userid', None)
    
    if user_id:
        try:
            user = User.objects.get(id=user_id)
            if user.is_admin:
                return True
        except User.DoesNotExist:
            pass

    return False


def list(request):
    if not is_admin(request):
        return render(request, 'not_admin.html')
    order_list = Order.objects.all().order_by('id')
    # Pagination    
    paginator = Paginator(order_list, 10)  # Display 10 products per page
    page = request.GET.get('page') or 1  # If the requested page number is not set or is an empty string, set to 1


    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        # If the requested page number is not an integer, the first page is displayed
        orders = paginator.page(1)
    except EmptyPage:
        # If the requested page number is out of range, the last page will be displayed
        orders = paginator.page(paginator.num_pages)

    
    return render(request, 'admin_list.html',{'orders':orders})



def userList(request):
    if not is_admin(request):
        return render(request, 'not_admin.html')
    user_list = User.objects.all().order_by('id')
    # Pagination    
    paginator = Paginator(user_list, 10)  # Display 10 products per page
    page = request.GET.get('page') or 1  # If the requested page number is not set or is an empty string, set to 1


    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        # If the requested page number is not an integer, the first page is displayed
        users = paginator.page(1)
    except EmptyPage:
        # If the requested page number is out of range, the last page will be displayed
        users = paginator.page(paginator.num_pages)

    
    return render(request, 'user_list.html',{'users':users})


def dashboard(request):
    if not is_admin(request):
        return render(request, 'not_admin.html')
    orders = Order.objects.all().order_by('order_date')
    data = [
        go.Scatter(
            x=[order.order_date for order in orders],
            y=[order.product_quantity for order in orders],
            name='Quantity',
            mode='lines'
        ),
        go.Scatter(
            x=[order.order_date for order in orders],
            y=[order.product_price for order in orders],
            name='Price',
            mode='lines'
        )
    ]
    layout = go.Layout(
        title='Sales Over Time',
        xaxis=dict(title='Date'),
        yaxis=dict(title='Sales')
    )
    chart = plot(go.Figure(data=data, layout=layout), output_type='div')


    return render(request, 'dashboard.html', {'chart': chart})

