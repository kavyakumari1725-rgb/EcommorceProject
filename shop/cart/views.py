from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.catalog.models import Product
from .cart import Cart  # ✅ ensure you import your Cart class

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product.id)
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    Cart(request).remove(product_id)
    return redirect('cart:cart_detail')

def cart_clear(request):
    Cart(request).clear()
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
