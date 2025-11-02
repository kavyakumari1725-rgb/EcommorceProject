from django import forms

class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=60)
    last_name = forms.CharField(max_length=60)
    email = forms.EmailField()
    address = forms.CharField(max_length=250)
    city = forms.CharField(max_length=120)
    postal_code = forms.CharField(max_length=20)
