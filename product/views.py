from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializers
from django.http import JsonResponse
from django.db.models import Count, Avg
from product.models import Product, Category

# Create your views here.

@api_view(['GET'])
def test_api_view(request):
    dict_ = {
        'first_name' : 'Azamat',
        'age' : 19,
        'gpa' : 3.7,
        'married' : False,
        'friends' : ['Azat', 'Mariya']
    }
    return Response(data=dict_)

@api_view(['GET'])
def product_list_api_view(request):
    product_list = Product.objects.all()
    data = ProductSerializers(product_list, many=True).data
    return Response(data=data)

def category_list(request):
    categories = Category.objects.annotate(products_count=Count('product'))
    data = [{'name': category.name, 'products_count': category.products_count} for category in categories]
    return JsonResponse(data, safe=False)

def product_reviews(request):
    products = Product.objects.all()
    data = []
    for product in products:
        reviews = product.review_set.all()
        reviews_data = [{'text': review.text, 'stars': review.stars} for review in reviews]
        avg_rating = reviews.aggregate(Avg('stars'))['stars__avg']
        data.append({'title': product.title, 'reviews': reviews_data, 'rating': avg_rating})
    return JsonResponse(data, safe=False)