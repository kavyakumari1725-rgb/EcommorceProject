from django.test import TestCase
from django.urls import reverse
from shop.catalog.models import Product

class CatalogIntegrationTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            slug="test-product",
            price=10.99,
            is_active=True
        )

    def test_product_list_and_detail_flow(self):
        list_url = reverse("catalog:product_list")
        list_response = self.client.get(list_url)
        self.assertEqual(list_response.status_code, 200)
        self.assertContains(list_response, "Test Product")

        detail_url = reverse("catalog:product_detail", args=[self.product.slug])
        detail_response = self.client.get(detail_url)
        self.assertEqual(detail_response.status_code, 200)
        self.assertContains(detail_response, "Test Product")
