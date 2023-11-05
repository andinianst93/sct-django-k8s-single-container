from django.urls import path, include
from .views import Products

urlpatterns = [
    path('', Products.as_view(), name="products"),
]