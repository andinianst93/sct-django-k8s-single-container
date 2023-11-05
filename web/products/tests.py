from django.test import TestCase
from .models import CustomUser, Product

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

    def test_add_product(self):
        # Login the user
        self.client.login(username="testuser", password="testpassword")

        # Create a new product
        response = self.client.post('/add_product/', {
            'name': 'New Product',
            'description': 'Description for New Product',
            'price': '25.99',
            'quantity': '30'
        })

        # Check if the product was added successfully
        self.assertEqual(response.status_code, 302)  # 302 is the status code for a successful redirect

        # Check if the product exists in the database
        new_product = Product.objects.get(name='New Product')
        self.assertEqual(new_product.description, 'Description for New Product')

    def test_display_products(self):
        # Make a GET request to the product listing page
        response = self.client.get('/products/')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check how many products are displayed in the response
        products = response.context['products']
        self.assertEqual(len(products), 2)  # Assuming there are two products in the database

        # Check if the product names are in the response content
        self.assertContains(response, 'Product 1')
        self.assertContains(response, 'Product 2')

        # You can add more assertions as needed to check the display of other product details

# Replace '/add_product/' and '/products/' with the actual URL patterns you have in your Django project.
