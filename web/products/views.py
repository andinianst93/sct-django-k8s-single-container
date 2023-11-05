from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from .models import Product
from .serializers import ProductsSerializer
from .pagination import CustomPagination

class Products(generics.ListAPIView):
    serializer_class = ProductsSerializer
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    pagination_class = CustomPagination
