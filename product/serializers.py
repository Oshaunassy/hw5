from rest_framework import serializers
from .models import Product, Review, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name birth_year'.split()

class ProductSerializers(serializers.ModelSerializer):
    category = CategorySerializer
    class Meta:
        model = Product
        fields = 'id title price'.split()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'product stars'.split()

class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100, min_length=3)
    description = serializers.CharField(required=False)
    produced = serializers.DateField()
    price = serializers.DecimalField(required=True)
    category = serializers.CharField(max_length=100)

