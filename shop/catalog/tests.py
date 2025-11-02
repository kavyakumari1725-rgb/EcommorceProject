from django.test import TestCase
from django.urls import reverse
from .models import Category, Product

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics", slug="electronics")

    def test_str_method(self):
        """Category name should be returned in string representation"""
        self.assertEqual(str(self.category), "Electronics")

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Books", slug="books")
        self.product = Product.objects.create(
            category=self.category,
            name="Python 101",
            slug="python-101",
            price=29.99,
            stock=10,
            is_active=True,
        )

    def test_str_method(self):
        """Product name should be returned in string representation"""
        self.assertEqual(str(self.product), "Python 101")

    def test_get_absolute_url(self):
        """Product should generate correct detail URL"""
        url = self.product.get_absolute_url()
        self.assertTrue(url.endswith("/python-101/"))

class CatalogViewsTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Shoes", slug="shoes")
        self.product = Product.objects.create(
            category=self.category,
            name="Running Shoes",
            slug="running-shoes",
            price=59.99,
            stock=5,
            is_active=True,
        )

    def test_product_list_page(self):
        """Product list view should display all products"""
        response = self.client.get(reverse("catalog:product_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Running Shoes")

    def test_product_detail_page(self):
        """Product detail view should display a single product"""
        response = self.client.get(reverse("catalog:product_detail", args=[self.product.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Running Shoes")
        self.assertContains(response, "£59.99")
