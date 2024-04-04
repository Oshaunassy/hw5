
from django.urls import path
from product import views

appname = 'product'
urlpatterns = [
    path('list/', views.product_list_api_view),
    path('detail/', views.product_detail_api_view),
    path('', views.ProductListCreateAPIView.as_view()),
    path('category/', views.CategoryListAPIView.as_view()),
    path('category/<int:id>/', views.CategoryDetailAPIView.as_view()),
    path('category/', views.CategoryAPIViewSet.as_view({
        'get':'list',
        'post': 'create'
    })),
    path('category/<int:id>/', views.CategoryAPIViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]
