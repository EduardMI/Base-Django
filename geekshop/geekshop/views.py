from django.shortcuts import render
from mainapp.models import Product

def index(request):
    title = 'geekshop'
    products = Product.objects.all()

    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'geekshop/index.html', context=context)

def contact(request):
    title = 'контакты'

    context = {
        'title': title,
    }
    return render(request, 'geekshop/contact.html', context=context)