from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}

class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)  
    class Meta:
        model = Order
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}