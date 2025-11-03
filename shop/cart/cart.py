from decimal import Decimal
from shop.catalog.models import Product

CART_SESSION_ID = 'cart'

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product_id, quantity=1, override=False):
        product = Product.objects.get(pk=product_id)
        item = self.cart.get(str(product_id), {'quantity': 0, 'price': str(product.price)})
        item['quantity'] = quantity if override else item['quantity'] + quantity
        self.cart[str(product_id)] = item
        self.save()

    def remove(self, product_id):
        self.cart.pop(str(product_id), None)
        self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for p in products:
            item = self.cart[str(p.id)]
            item['product'] = p
            item['total_price'] = Decimal(item['price']) * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        from decimal import Decimal
        return sum(Decimal(i['price']) * i['quantity'] for i in self.cart.values())

    def clear(self):
        self.session[CART_SESSION_ID] = {}
        self.save()

    def save(self):
        self.session.modified = True