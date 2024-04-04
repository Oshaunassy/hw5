from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializers, CategorySerializer
from django.http import JsonResponse
from django.db.models import Count, Avg
from product.models import Product, Category
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class CategoryAPIViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'

class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.select_related('category') \
        .prefetch_related('reviews', 'category').all()
    serializer_class = ProductSerializers

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': serializer.errors})

        product = request.validated_data.get('product')
        description = request.validated_data.get('description')
        produced = request.validated_data.get('produced')
        price = request.validated_data.get('price')
        category = request.validated_data.get('category')

        product = Product.objects.create(product=product, description=description, produced=produced,
                                         price=price, category=category)
        product.category.set(category)
        product.save()

        return Response(data={'product_id': product.id})


class CategoryListAPIView(ListAPIView, CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


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

@api_view(['GET', 'POST'])
def product_list_api_view(request):
    print(request.user)
    if request.method == 'GET':
        product_list = Product.objects.all()
        data = ProductSerializers(instance=product_list, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = ProductSerializers(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': serializer.errors})

        product = request.validated_data.get('product')
        description = request.validated_data.get('description')
        produced = request.validated_data.get('produced')
        price = request.validated_data.get('price')
        category = request.validated_data.get('category')

        product = Product.objects.create(product=product, description=description, produced=produced,
                                         price=price, category=category)
        product.category.set(category)
        product.save()

        return Response(data={'product_id': product.id})

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        product_detail = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error_message': 'Product not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data=ProductSerializers(product_detail).data
        return Response(data=data)
    elif request.method == 'PUT':
        product_detail.product = request.data.get('product')
        product_detail.description = request.data.get('description')
        product_detail.produced = request.data.get('produced')
        product_detail.price = request.data.get('price')
        product_detail.category = request.data.get('category')
        product_detail.save()
        return Response(status=status.HTTP_201_CREATED, data={'product_id': product_detail.id})
    else:
        product_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
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