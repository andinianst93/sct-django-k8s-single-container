from rest_framework import serializers
from .models import Product, CustomUser

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "quantity"]