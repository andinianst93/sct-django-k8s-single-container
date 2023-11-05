from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True, null=False)
    email = models.TextField(unique=True, null=False)
    password = models.TextField(null=False)
    fullname = models.TextField()

    def __str__(self):
        return self.username

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name
