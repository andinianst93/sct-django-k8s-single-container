from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Product
# Register your models here.
User = get_user_model()
admin.site.register(User)
admin.site.register(Product)
