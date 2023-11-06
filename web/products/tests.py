from django.test import TestCase
from .models import CustomUser, Product
import json

class ProductTestCase(TestCase):
    def setUp(self):
        # Create a custom user for testing
        self.user = CustomUser.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword",
            fullname="Test User"
        )

        # Create some products for testing
        self.product1 = Product.objects.create(
            name="Product 1",
            description="Description for Product 1",
            price=10.99,
            quantity=20
        )
        self.product2 = Product.objects.create(
            name="Product 2",
            description="Description for Product 2",
            price=15.99,
            quantity=15
        )

    def test_display_products(self):
        # Make a GET request to the product listing page
        response = self.client.get('/api/')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Parse the JSON response content
        content = json.loads(response.content)

        # Check if the 'results' key exists in the JSON content
        self.assertTrue('results' in content)

        # Check the number of products in the API
        products = content['results']
        self.assertEqual(len(products), 2) 

        # Check if the product names are in the JSON response
        product_names = [product['name'] for product in products]
        self.assertIn('Product 1', product_names)
        self.assertIn('Product 2', product_names)


