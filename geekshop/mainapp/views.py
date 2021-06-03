from django.shortcuts import render
from .models import ProductCategory, Product

def products(request, pk=None):
    title = 'каталог'
    categories = ProductCategory.objects.all()
    links_menu = [{'href': '/products/', 'name': 'все'}]

    # links_menu = [
    #     {'href': 'category', 'name': 'все'},
    #     {'href': '/products/1/', 'name': 'дом'},
    #     {'href': '/products/2', 'name': 'офис'},
    #     {'href': '/products/3', 'name': 'модерн'},
    #     {'href': '/products/4', 'name': 'классика'},
    # ]
    for item in categories:
        temp_dict = {}
        temp_dict['href'] = f'/products/{item.pk}/'
        temp_dict['name'] = f'{item.name}'
        links_menu.append(temp_dict)



    if pk:
        category = ProductCategory.objects.get(pk=pk)
        product = Product.objects.all()
        context = {
            'title': title,
            'links_menu': links_menu,
            'product': product,
            'category': category,
        }
        return render(request, 'mainapp/category.html', context=context)

    context = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, 'mainapp/products.html', context=context)
