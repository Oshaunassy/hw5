from rest_framework import serializers
from .models import Product, Review, Category, Price

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name birth_year'.split()

class ProductSerializers(serializers.ModelSerializer):
    category = CategorySerializer

    class Meta:
        model = Product
        fields = 'id title price'.split()

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = 'id name'.split()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'product stars'.split()

class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100, min_length=3)
    description = serializers.CharField(required=False)
    produced = serializers.DateField()
    price = serializers.DecimalField(required=True, decimal_places=2, max_digits=10)
    category = serializers.CharField(max_length=100)

