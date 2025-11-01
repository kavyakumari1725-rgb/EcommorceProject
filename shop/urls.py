from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.catalog.urls', namespace='catalog')),
    path('cart/', include('shop.cart.urls', namespace='cart')),
    path('orders/', include('shop.orders.urls', namespace='orders')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
