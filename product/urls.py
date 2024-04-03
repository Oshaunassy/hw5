
from django.urls import path
from product import views

appname = 'product'
urlpatterns = [
    path('list/', views.product_list_api_view),
    path('detail/', views.product_detail_api_view)
]
