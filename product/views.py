from django.shortcuts import render
from parse_data.models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import sqlite3
import re
# Create your views here.
def index(request):
    products_list = Product.objects.all().order_by('id')

    # Search
    search_query = request.GET.get('search_query')
    if search_query is not None:
        search_query_digits = re.findall(r'\d+', search_query)
        if search_query_digits:
            search_query = int(search_query_digits[0])
        else:
            search_query = None

    search_field = 'id'
    if search_query:
        products_list = products_list.filter(**{f"{search_field}__icontains": search_query})

     # Pagination    
    paginator = Paginator(products_list, 8)  # Display 8 products per page
    page = request.GET.get('page') or 1  # If the requested page number is not set or is an empty string, set to 1
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If the requested page number is not an integer, the first page is displayed
        products = paginator.page(1)
    except EmptyPage:
        # If the requested page number is out of range, the last page will be displayed
        products = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'products':products,'search_query': search_query})

def detail(request,id):
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    cursor.execute('SELECT a.id, a.currency, a.price, a.rating_count_tot, a.user_rating, b.size_bytes, b.rating_count_ver, b.user_rating_ver, b.ver, b.cont_rating, b.prime_genre, b.sup_devices_num, b.ipadSc_urls_num, b.lang_num, b.vpp_lic FROM product AS a LEFT JOIN product_detail AS b ON a.id = b.product_id_id WHERE a.id = ?', (id,))
    detail = cursor.fetchone()
    connection.close()
    detail_dict = {
        'id': detail[0],
        'currency': detail[1],
        'price': detail[2],
        'rating_count_tot': detail[3],
        'user_rating': detail[4],
        'size_bytes': detail[5],
        'rating_count_ver': detail[6],
        'user_rating_ver': detail[7],
        'ver': detail[8],
        'cont_rating': detail[9],
        'prime_genre': detail[10],
        'sup_devices_num': detail[11],
        'ipadSc_urls_num': detail[12],
        'lang_num': detail[13],
        'vpp_lic': detail[14],
        'img_url': get_image_url(detail[10], genre_image_mapping),
    }
   
    return render(request, 'detail.html', {'detail': detail_dict})

genre_image_mapping = {
    '0': 'https://images.unsplash.com/photo-1503428593586-e225b39bddfe?auto=format&fit=crop&w=700&q=60',
    '1': 'https://images.unsplash.com/photo-1555685812-4b943f1cb0eb?auto=format&fit=crop&w=700&q=60',
    '2': 'https://images.unsplash.com/photo-1501594907352-04cda38ebc29?auto=format&fit=crop&w=700&q=60',
    '3': 'https://plus.unsplash.com/premium_photo-1669349127566-9be644ceac6e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=880&q=80',
    '4': 'https://images.unsplash.com/photo-1610072947120-8736bbfc56e1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=730&q=80',
    '5': 'https://plus.unsplash.com/premium_photo-1670044020191-934d7264fc85?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1615&q=80',
    'Book': 'https://images.unsplash.com/photo-1516979187457-637abb4f9353?auto=format&fit=crop&w=700&q=60',
    'Business': 'https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=700&q=60',
    'Catalogs': 'https://plus.unsplash.com/premium_photo-1661964088064-dd92eaaa7dcf?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1112&q=80',
    'Education': 'https://images.unsplash.com/photo-1532012197267-da84d127e765?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
    'Entertainment': 'https://plus.unsplash.com/premium_photo-1680981143179-8a6cd94d2901?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8RW50ZXJ0YWlubWVudHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60',
    'Finance': 'https://images.unsplash.com/photo-1661956602868-6ae368943878?ixlib=rb-4.0.3&ixid=MnwxMjA3fDF8MHxzZWFyY2h8MXx8RmluYW5jZXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60',
    'Food & Drink': 'https://plus.unsplash.com/premium_photo-1674228288173-519727295a6c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8Zm9vZCUyMGRyaW5rfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60',
    'Games': 'https://images.unsplash.com/photo-1577741314755-048d8525d31e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80',
    'Health & Fitness': 'https://images.unsplash.com/photo-1483721310020-03333e577078?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8SGVhbHRoJTIwJTI2JTIwRml0bmVzc3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60',
    'Lifestyle': 'https://images.unsplash.com/photo-1529333166437-7750a6dd5a70?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8TGlmZXN0eWxlfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60',
    'Medical': 'https://images.unsplash.com/photo-1505751172876-fa1923c5c528?auto=format&fit=crop&w=700&q=60',
    'Music': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=700&q=60',
    'Navigation': 'https://images.unsplash.com/photo-1574158622682-e40e69881006?auto=format&fit=crop&w=700&q=60',
    'News': 'https://images.unsplash.com/photo-1495020689067-958852a7765e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1169&q=80',
    'Photo & Video': 'https://plus.unsplash.com/premium_photo-1673356713416-a8ed69af6f4a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8cGhvdG8lMjB2aWRlb3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60',
    'Productivity': 'https://images.unsplash.com/photo-1661956601030-fdfb9c7e9e2f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDF8MHxzZWFyY2h8MXx8cHJvZHVjdGl2aXR5fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60',
    'Reference': 'https://images.unsplash.com/photo-1559181567-c3190ca9959b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OHx8cmVmZXJlbmNlfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60',
    'Shopping': 'https://plus.unsplash.com/premium_photo-1672883551968-dd15ceb7f802?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8c2hvcHBpbmd8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60',
    'Social Networking': 'https://plus.unsplash.com/premium_photo-1663012925068-218ef7c0b4b7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8U29jaWFsJTIwTmV0d29ya2luZ3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60',
    'Sports': 'https://images.unsplash.com/photo-1517649763962-0c623066013b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8U3BvcnRzfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60',
    'Travel': 'https://images.unsplash.com/photo-1488646953014-85cb44e25828?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8VHJhdmVsfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60',
    'Utilities': 'https://images.unsplash.com/photo-1604177420682-0c840feb01de?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8VXRpbGl0aWVzfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60',
    'Weather': 'https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=700&q=60',
}

def get_image_url(prime_genre, genre_image_mapping):
    if prime_genre in genre_image_mapping:
        return genre_image_mapping[prime_genre]
    else:
        return 'https://example.com/images/default.jpg'

