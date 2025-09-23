from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from shop.models import Product, Category


def product_list(request, category_slug=None):

    debug_static_paths(request)

    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'products': products,
                   'category': category,
                   'categories': categories})

from django.conf import settings

def debug_static_paths(request):
    print("STATIC_URL:", settings.STATIC_URL)
    print("STATIC_ROOT:", settings.STATIC_ROOT)
    return HttpResponse("Проверка завершена")

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product, 'id': id, 'slug': slug,
                   'cart_product_form': cart_product_form})