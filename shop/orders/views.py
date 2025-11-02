from django.shortcuts import render, redirect
from django.contrib import messages
from shop.cart.cart import Cart
from .forms import CheckoutForm
from .models import Order, OrderItem


def checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(**form.cleaned_data, paid=True)  # mark paid for demo
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product_name=item['product'].name,
                    price=item['product'].price,
                    quantity=item['quantity']
                )
            cart.clear()
            messages.success(request, f'Thanks! Order #{order.id} placed.')
            return redirect('orders:success')
    else:
        form = CheckoutForm()
    return render(request, 'orders/checkout.html', {'form': form, 'cart': cart})


def success(request):
    return render(request, 'orders/success.html')
