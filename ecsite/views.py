from django.shortcuts import render
from store.models import Product

def home(requeset):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products': products, 
    }

    return render(requeset, 'home.html', context)