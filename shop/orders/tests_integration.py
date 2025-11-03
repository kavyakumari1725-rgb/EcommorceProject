from django.test import TestCase
from django.urls import reverse
from shop.catalog.models import Product, Category
from shop.orders.models import Order

class OrderIntegrationTests(TestCase):
    def setUp(self):
        # Create a category because Product.category is required
        self.category = Category.objects.create(
            name="Clothing",
            slug="clothing"
        )

        self.product = Product.objects.create(
            category=self.category,
            name="Order Product",
            slug="order-product",
            price=25.00,
            is_active=True
        )

    def test_order_creation_flow(self):
        # Add product to cart
        self.client.post(reverse("cart:cart_add", args=[self.product.id]), {"quantity": 1})

        # Create an order
        response = self.client.post(reverse("orders:checkout"), {
            "first_name": "Kalpana",
            "last_name": "Kumari",
            "email": "test@example.com",
            "address": "123 Street",
            "postal_code": "RM26BU",
            "city": "Romford"
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Order.objects.exists())