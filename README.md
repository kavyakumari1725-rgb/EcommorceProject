# Django E‑commerce Starter

A minimal, batteries-included Django shop: products, cart (session-based), and a dummy checkout that creates orders.

## Quickstart

```bash
python -m venv .venv && . .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/ and add products via `/admin/`.

## Apps

- `catalog`: Categories & Products
- `cart`: Session cart with add/remove/clear
- `orders`: Checkout form -> Order + OrderItems (no real payment yet)

## Next steps

- Wire in Stripe (webhooks & real payment).
- Add stock checks and decrement on purchase.
- SEO-friendly category pages.
- Email invoices, order status pages.
- Shipping/tax rules for your region.
