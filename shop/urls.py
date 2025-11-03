from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cart/", include(("shop.cart.urls", "cart"), namespace="cart")),
    path("catalog/", include(("shop.catalog.urls", "catalog"), namespace="catalog")),
    path("orders/", include(("shop.orders.urls", "orders"), namespace="orders")),
    path('', include('django_prometheus.urls')),
]

# ✅ Correct way to append static() URLs
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
