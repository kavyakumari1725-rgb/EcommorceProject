from django.test import TestCase
from django.urls import reverse
from shop.catalog.models import Product

class CartIntegrationTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Cart Product",
            slug="cart-product",
            price=15.00,
            is_active=True
        )

    def test_add_to_cart_and_view(self):
        add_url = reverse("cart:cart_add", args=[self.product.id])
        response = self.client.post(add_url, {"quantity": 2}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cart Product")

        cart_url = reverse("cart:cart_detail")
        response = self.client.get(cart_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cart Product")

    def test_remove_from_cart(self):
        add_url = reverse("cart:cart_add", args=[self.product.id])
        self.client.post(add_url, {"quantity": 1}, follow=True)

        remove_url = reverse("cart:cart_remove", args=[self.product.id])
        response = self.client.post(remove_url, follow=True)
        self.assertEqual(response.status_code, 200)
