from django.test import TestCase
from django.urls import reverse
from shop.catalog.models import Product, Category

class CartIntegrationTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category", slug="test-category")
        self.product = Product.objects.create(
            category=self.category,
            name="Test Product",
            slug="test-product",
            price=10.00
        )

    def test_add_to_cart_and_view(self):
        add_url = reverse("cart:cart_add", args=[self.product.id])  # ✅ fixed
        response = self.client.post(add_url)
        self.assertEqual(response.status_code, 302)

    def test_remove_from_cart(self):
        add_url = reverse("cart:cart_add", args=[self.product.id])  # ✅ fixed
        self.client.post(add_url)
        remove_url = reverse("cart:cart_remove", args=[self.product.id])  # ✅ fixed
        response = self.client.post(remove_url)
        self.assertEqual(response.status_code, 302)
