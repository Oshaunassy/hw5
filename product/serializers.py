from rest_framework import serializers
from .models import Product, Review

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id title price'.split()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'product stars'.split()

