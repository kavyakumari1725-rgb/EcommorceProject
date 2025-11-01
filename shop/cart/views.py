from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from .cart import Cart

@require_POST
def cart_add(request, product_id):
    quantity = int(request.POST.get('quantity', 1))
    Cart(request).add(product_id, quantity)
    return redirect('cart:detail')

def cart_remove(request, product_id):
    Cart(request).remove(product_id)
    return redirect('cart:detail')

def cart_clear(request):
    Cart(request).clear()
    return redirect('cart:detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
